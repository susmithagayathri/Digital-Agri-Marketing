"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('action_page/',views.action_page),
    path('about/',views.About),
    path('action_page/',views.action_page),
    path('register/',views.register,name="register"),
    path('action_page/',views.action_page),
    path('login/',views.login ,name="login"),
    path('gallery/',views.gallery),
    path('shop/',views.shop),
    path('shop-detail/',views.shopdetail),
    path('cart/',views.Cart),
    path('checkout/',views.checkout),
    path('my-account/',views.myaccount),
    path('wishlist/',views.wishlist),
    path('action_page/',views.action_page),
    path('contact-us/',views.contactus),
    
]

