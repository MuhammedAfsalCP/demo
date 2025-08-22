from django.contrib import admin
from .models import (
    Category, Product, HeroSection, AboutSection, FooterLink, NewsletterSubscriber,
    SiteTheme, SiteLogo, NavLink, SocialLink, SiteSettings,
    Banner, Offer, Order, OrderItem,
    FeaturedProduct, BestSeller, NewArrival,
    ProductReview, AboutPage, ContactMessage
)

# ----------------- CATEGORY & PRODUCT -----------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "stock", "available")
    list_filter = ("available", "category")
    search_fields = ("name", "description")

# ----------------- HERO & ABOUT -----------------
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)  # removed "updated_at" if not in model

# ----------------- FOOTER -----------------
@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "url")  # removed "order" if not in model
    # list_editable removed if "order" not in model

# ----------------- SITE SETTINGS -----------------
@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ("primary_color", "secondary_color", "text_color")

@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ("logo", "alt_text")

@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "url")  # removed "order" if not in model

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_title",)

# ----------------- HOME BANNERS & OFFERS -----------------
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "active")  # removed "order" if not in model
    list_editable = ("active",)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("title", "active")  # removed "order" if not in model
    list_editable = ("active",)

# ----------------- NEWSLETTER -----------------
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "date_subscribed")
    search_fields = ("email",)

# ----------------- ORDERS -----------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_amount", "payment_status", "date_ordered")
    list_filter = ("payment_status", "date_ordered")
    search_fields = ("user__username", "id")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")

# ----------------- FEATURED / BESTSELLER / NEW ARRIVAL -----------------
@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ("product", "active")  # removed "order" if not in model
    list_editable = ("active",)

@admin.register(BestSeller)
class BestSellerAdmin(admin.ModelAdmin):
    list_display = ("product", "active")  # removed "order" if not in model
    list_editable = ("active",)

@admin.register(NewArrival)
class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ("product", "active")  # removed "order" if not in model
    list_editable = ("active",)

# ----------------- PRODUCT REVIEWS -----------------
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "approved", "date_posted")
    list_editable = ("approved",)
    list_filter = ("approved", "date_posted")
    search_fields = ("product__name", "user__username")

# ----------------- ABOUT PAGE -----------------
@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("title",)  # removed "updated_at" if not in model

# ----------------- CONTACT MESSAGES -----------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)
