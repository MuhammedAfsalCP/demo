from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path("cart/increase/<int:product_id>/", views.increase_quantity, name="increase_quantity"),
    path("cart/decrease/<int:product_id>/", views.decrease_quantity, name="decrease_quantity"),


    path('checkout/', views.checkout, name='checkout'),
    path('payment_success/', views.payment_success, name='payment_success'),

    path('shop/search/', views.shop_search, name='shop_search'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
     path('logout/', logout_view, name='logout'),
    path('orders/', views.order_history, name='order_history'),
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

     path('register/', views.register, name='register'),
]
