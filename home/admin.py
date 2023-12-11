from django.contrib import admin
from home.models import Contact
from home.models import Author, Product

# Register your models ere.
admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Product)