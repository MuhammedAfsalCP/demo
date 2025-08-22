from django.shortcuts import render
from .models import HeroSection, Category, Product, AboutSection
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

#razorpay
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product

from django.db.models import Q

from django.core.paginator import Paginator

from .models import Banner, Offer, SiteTheme

def home(request):
    hero_slides = HeroSection.objects.filter(active=True)
    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)
    about = AboutSection.objects.first()  # assuming only one About section
    banners = Banner.objects.filter(active=True)
    offers = Offer.objects.filter(active=True)
    theme = SiteTheme.objects.first()  # assume only one row

    context = {
        'hero_slides': hero_slides,
        'categories': categories,
        'featured_products': featured_products,
        'about': about,
        banners': banners,
        'offers': offers,
        'theme': theme,
        
    }
    return render(request, 'store/home.html', context)



# ----------------- SHOP PAGE -----------------
def shop(request):
    category_id = request.GET.get('category')
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.all()

    # Pagination
    paginator = Paginator(products, 8)  # 8 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
        'page_obj': page_obj,  # for template pagination
    }
    return render(request, 'store/shop.html', context)

# ----------------- PRODUCT DETAIL -----------------
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
        total += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': product.price * quantity})
    context = {'cart_items': cart_items, 'total': total}
    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart')

#razorpay
# ----------------- CHECKOUT -----------------
def checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    total_amount = sum(product.price * cart[str(product.id)] for product in products)
    total_amount_paise = int(total_amount * 100)  # Razorpay requires paisa

    # Create Razorpay client & order
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

# ----------------- PAYMENT SUCCESS -----------------
def payment_success(request):
    # Clear cart after payment
    request.session['cart'] = {}
    return render(request, 'store/payment_success.html')



#searchbar
# ----------------- SEARCH -----------------
def shop_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'query': query,
    }
    return render(request, 'store/shop.html', context)