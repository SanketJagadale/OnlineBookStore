from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'selling_price', 'discounted_price',  'description', 'books', 'category', 'product_image']