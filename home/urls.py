from django.contrib import admin
from django.urls import path
from home import views

app_name='home'

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("product", views.product, name='product'),
    path("contact/", views.contact, name='contact'),
    path("contact", views.contact, name='contact'),
    path("search", views.search, name='search'),
    path("signup", views.Signup, name='Signup'),
    path("login", views.handlelogin, name='handlelogin'),
    path("logout", views.handlelogout, name='handlelogout')
 
]


