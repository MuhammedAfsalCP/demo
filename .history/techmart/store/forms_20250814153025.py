from django import forms
from .models import NewsletterSubscriber
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProductReview

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your review here...'}),
        }