from django.urls import path,include
from . import views

urlpatterns = [
    path('products',views.products,name='products'),
    path('additem',views.additem,name='additem'),
    path('addwatches',views.addwatches,name='addwatches'),
    path('addcloths',views.addcloths,name='addcloths'),
    
]
