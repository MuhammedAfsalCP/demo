from django.db import models
from django.contrib.auth.models import User

# ----------------- CATEGORY -----------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# ----------------- PRODUCT -----------------
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


# ----------------- CART -----------------
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Cart ({self.user.username})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)  # Ensure Product is defined
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

# ----------------- HERO SECTION -----------------
class HeroSection(models.Model):
    headline = models.CharField(max_length=200)
    sub_text = models.CharField(max_length=300, blank=True)
    background_image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=50, blank=True)
    button_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.headline


# ----------------- ABOUT SECTION -----------------
class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title


# ----------------- FOOTER LINKS -----------------
class FooterLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


# ----------------- NEWSLETTER -----------------
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# ----------------- SITE COLORS / THEME -----------------
class SiteTheme(models.Model):
    primary_color = models.CharField(max_length=7, default="#1D4ED8")  # Tailwind blue
    secondary_color = models.CharField(max_length=7, default="#FBBF24")  # Tailwind yellow
    text_color = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return "Site Theme"


# ----------------- SITE LOGO -----------------
class SiteLogo(models.Model):
    logo = models.ImageField(upload_to="site_logo/")
    alt_text = models.CharField(max_length=50, default="TechMart Logo")

    def __str__(self):
        return "Site Logo"


# ----------------- NAVBAR LINKS -----------------
class NavLink(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ----------------- SOCIAL LINKS -----------------
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name


# ----------------- SITE SETTINGS -----------------
class SiteSettings(models.Model):
    site_title = models.CharField(max_length=100, default="TechMart")

    def __str__(self):
        return self.site_title


# ----------------- HOME BANNERS -----------------
class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='banners/images/', blank=True, null=True)
    video = models.FileField(upload_to='banners/videos/', blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True)
    button_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# ----------------- OFFERS -----------------
class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='offers/')
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ----------------- ORDERS -----------------
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"


# ----------------- FEATURED / BESTSELLER / NEW ARRIVAL -----------------
class FeaturedProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Featured: {self.product.title}"


class BestSeller(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Best Seller: {self.product.title}"


class NewArrival(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"New Arrival: {self.product.title}"


# ----------------- PRODUCT REVIEWS -----------------
class ProductReview(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)  # 1-5 stars
    review = models.TextField()
    approved = models.BooleanField(default=False)  # Admin must approve
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


# ----------------- ABOUT PAGE -----------------
class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="About Tech Computers")
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ----------------- CONTACT MESSAGES -----------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)  # 👈 add this
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"