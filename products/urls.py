from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('book/', views.books, name='book'),
    path('book/<slug:data>', views.books, name='bookdata'),    
]
