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
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# ----------------- SITE COLORS -----------------
class SiteTheme(models.Model):
    primary_color = models.CharField(max_length=7, default="#1D4ED8")  # Tailwind blue
    secondary_color = models.CharField(max_length=7, default="#FBBF24")  # Tailwind yellow
    text_color = models.CharField(max_length=7, default="#000000")
    
    def __str__(self):
        return "Site Theme"

# ----------------- HOME BANNERS -----------------
class Banner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, blank=True)
    button_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

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
    

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


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


class ProductReview(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)  # 1-5 stars
    review = models.TextField()
    approved = models.BooleanField(default=False)  # Admin must approve
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"