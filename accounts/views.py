from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import Customer
from cart.models import Cart
from .forms import SignupForm,CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'accounts/customerregistration.html', {'form':form})
  
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully.')
            form.save()
        return render(request, 'accounts/customerregistration.html', {'form':form})




@method_decorator(login_required, name='dispatch')
class ProfileView(View):
	def get(self, request):
		totalitem = 0
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		form = CustomerProfileForm()
		return render(request, 'accounts/profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})
		
	def post(self, request):
		totalitem = 0
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		form = CustomerProfileForm(request.POST)
		if form.is_valid():
			usr = request.user
			name  = form.cleaned_data['name']
			locality = form.cleaned_data['locality']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			ContactNo=form.cleaned_data['ContactNo']
			reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode,ContactNo=ContactNo)
			reg.save()
			messages.success(request, 'Congratulations!! Profile Updated Successfully.')
		return render(request, 'accounts/profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})