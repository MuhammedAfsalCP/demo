from django.contrib import admin
from .models import Category, Product, HeroSection, AboutSection, FooterLink, NewsletterSubscriber
from .models import SiteTheme, Banner, Offer
from .models import Order, OrderItem
from .models import FeaturedProduct, BestSeller


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(HeroSection)
admin.site.register(AboutSection)
admin.site.register(FooterLink)
admin.site.register(NewsletterSubscriber)


@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ['primary_color', 'secondary_color', 'text_color']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'order']
    list_editable = ['active', 'order']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'order']
    list_editable = ['active', 'order']



@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_subscribed']



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'payment_status', 'date_ordered']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']


@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'active', 'order']
    list_editable = ['active', 'order']

@admin.register(BestSeller)
class BestSellerAdmin(admin.ModelAdmin):
    list_display = ['product', 'active', 'order']
    list_editable = ['active', 'order']