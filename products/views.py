from django.shortcuts import render
from .models import Product
from cart.models import Cart
from django.views import View
from django.db.models import Q
# Create your views here.

class ProductView(View):
    def get(self,request):
        totalitems=0
        bookst=Product.objects.filter(category='B')
        if request.user.is_authenticated:
            totalitems=len(Cart.objects.filter(user=request.user))
        return render(request,'product/home.html',{'bookst':bookst,'totalitems':totalitems})

class ProductDetailView(View):
    def get(self, request, pk):
	    totalitem = 0
	    product = Product.objects.get(pk=pk)
	    print(product.id)
	    item_already_in_cart=False
	    if request.user.is_authenticated:
		    totalitem = len(Cart.objects.filter(user=request.user))
		    item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
	    return render(request, 'product/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})



def books(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
	    totalitem = len(Cart.objects.filter(user=request.user))
    if data==None :
	    bookst = Product.objects.filter(category='B')
    elif data == 'Python' or data == 'Php' or data == 'Java':
	    bookst = Product.objects.filter(category='B').filter(books=data)
    elif data == 'below':
	    bookst = Product.objects.filter(category='B').filter(discounted_price__lt=300)
    elif data == 'above':
	    bookst = Product.objects.filter(category='B').filter(discounted_price__gt=300)
    return render(request, 'product/books.html', {'bookst':bookst, 'totalitem':totalitem})



'''
def search(request):
    queryset = Item.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search.html', context)
'''