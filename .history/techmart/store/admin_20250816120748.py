from django.contrib import admin
from .models import (
    Category, Product, HeroSection, AboutSection, FooterLink, NewsletterSubscriber,
    SiteTheme, SiteLogo, NavLink, SocialLink, SiteSettings,
    Banner, Offer, Order, OrderItem,
    FeaturedProduct, BestSeller, NewArrival,
    ProductReview, AboutPage, ContactMessage

)

# ----------------- CATEGORY & PRODUCT -----------------
admin.site.register(Category)
admin.site.register(Product)

# ----------------- HERO & ABOUT -----------------
admin.site.register(HeroSection)
admin.site.register(AboutSection)

# ----------------- FOOTER -----------------
admin.site.register(FooterLink)

# ----------------- SITE SETTINGS -----------------
@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ['primary_color', 'secondary_color', 'text_color']

@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ['logo', 'alt_text']

@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'order']
    list_editable = ['order']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title']

# ----------------- HOME BANNERS & OFFERS -----------------
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'order')
    list_editable = ('active', 'order')
    ordering = ('order',)
    
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'order']
    list_editable = ['active', 'order']

# ----------------- NEWSLETTER -----------------
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_subscribed']

# ----------------- ORDERS -----------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'payment_status', 'date_ordered']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

# ----------------- FEATURED / BESTSELLER / NEW ARRIVAL -----------------
@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'active', 'order']
    list_editable = ['active', 'order']

@admin.register(BestSeller)
class BestSellerAdmin(admin.ModelAdmin):
    list_display = ['product', 'active', 'order']
    list_editable = ['active', 'order']

@admin.register(NewArrival)
class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ['product', 'active', 'order']
    list_editable = ['active', 'order']

# ----------------- PRODUCT REVIEWS -----------------
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'approved', 'date_posted']
    list_editable = ['approved']
    list_filter = ['approved', 'date_posted']


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')