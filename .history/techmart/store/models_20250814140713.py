from django.db import models

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
