from django.shortcuts import render
from .models import HeroSection, Category, Product, AboutSection

def home(request):
    hero_slides = HeroSection.objects.filter(active=True)
    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)
    about = AboutSection.objects.first()  # assuming only one About section

    context = {
        'hero_slides': hero_slides,
        'categories': categories,
        'featured_products': featured_products,
        'about': about,
    }
    return render(request, 'store/home.html', context)
