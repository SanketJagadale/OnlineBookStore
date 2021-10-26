from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
  
  # Below Property will be used by checkout.html page to show total cost in order summary
@property
def total_cost(self):
   return self.quantity * self.product.discounted_price