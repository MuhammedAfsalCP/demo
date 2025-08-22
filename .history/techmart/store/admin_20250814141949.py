from django.contrib import admin
from .models import Category, Product, HeroSection, AboutSection, FooterLink, NewsletterSubscriber
from .models import SiteTheme, Banner, Offer


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(HeroSection)
admin.site.register(AboutSection)
admin.site.register(FooterLink)
admin.site.register(NewsletterSubscriber)
