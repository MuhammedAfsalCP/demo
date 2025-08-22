from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms

from .models import ContactMessage


import razorpay
from django.conf import settings
from django.contrib.auth import logout

from .models import (
    Cart, Product, AboutPage, ContactMessage,
    HeroSection, Category, AboutSection, Banner, Offer, SiteTheme,
    FeaturedProduct, BestSeller, NewArrival, Order, OrderItem
)
from .forms import NewsletterForm, ProductReviewForm


# ----------------- HOME -----------------
def home(request):
    hero_slides = HeroSection.objects.filter(active=True)
    categories = Category.objects.all()
    about = AboutSection.objects.first()  # assuming only one About section
    banners = Banner.objects.filter(active=True)
    offers = Offer.objects.filter(active=True)
    theme = SiteTheme.objects.first()
    featured_products = FeaturedProduct.objects.filter(active=True)
    best_sellers = BestSeller.objects.filter(active=True)
    new_arrivals = NewArrival.objects.filter(active=True)

    context = {
        'hero_slides': hero_slides,
        'categories': categories,
        'about': about,
        'banners': banners,
        'offers': offers,
        'theme': theme,
        'featured_products': featured_products,
        'best_sellers': best_sellers,
        'new_arrivals': new_arrivals,
    }
    return render(request, 'store/home.html', context)


# ----------------- STATIC PAGES -----------------
def about(request):
    about_page = AboutPage.objects.first()  # get first entry
    return render(request, "store/about.html", {"about_page": about_page})


# Contact Form (ModelForm)
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request, "There was an error. Please check the form.")
    else:
        form = ContactForm()
    return render(request, "store/contact.html", {"form": form})


def register(request):
    return render(request, 'store/register.html')


# ----------------- SHOP -----------------
def shop(request):
    category_id = request.GET.get('category')
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.all()

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
        'page_obj': page_obj,
    }
    return render(request, 'store/shop.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


# ----------------- CART -----------------
def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('shop')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart')


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            cart.pop(str(product_id), None)
        request.session['cart'] = cart
    return redirect('checkout')


# ----------------- CHECKOUT & RAZORPAY -----------------
def checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    total_amount = sum(product.price * cart[str(product.id)] for product in products)
    total_amount_paise = int(total_amount * 100)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    order = client.order.create({
        "amount": total_amount_paise,
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        'products': products,
        'cart': cart,
        'total_amount': total_amount,
        'order_id': order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
    }
    return render(request, 'store/checkout.html', context)


def payment_success(request):
    request.session['cart'] = {}
    return render(request, 'store/payment_success.html')


# ----------------- SEARCH -----------------
def shop_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories, 'query': query}
    return render(request, 'store/shop.html', context)


# ----------------- SIGNUP & PROFILE -----------------
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'store/profile.html')


# ----------------- NEWSLETTER -----------------
def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsletterForm()
    return render(request, 'store/newsletter.html', {'form': form})


# ----------------- ORDER HISTORY -----------------
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    return render(request, 'store/order_history.html', {'orders': orders})


# ----------------- PRODUCT REVIEW -----------------
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', pk=product.id)
    else:
        form = ProductReviewForm()
    return render(request, 'store/add_review.html', {'form': form, 'product': product})


def logout_view(request):
    if request.method == 'POST':  # important: POST only
        logout(request)
        return redirect('home')
    else:
        return redirect('home')  # optional fallback for GET requests
        

# ----------------- CART QUANTITY HANDLING -----------------
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem

def increase_quantity(request, product_id):
    cart_item = get_object_or_404(
        CartItem,
        cart__user=request.user,
        product_id=product_id
    )
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart_detail")  # or your cart page



def decrease_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("cart")


