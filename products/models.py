from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
 ('B', 'Books'),
)
class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 books = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
 product_image = models.ImageField(upload_to='media')

 def __str__(self):
  return str(self.id)