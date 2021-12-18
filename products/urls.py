from django.urls import path,include
from . import views

urlpatterns = [
    path('additem',views.additem,name='additem'),
    path('addwatches',views.addwatches,name='addwatches'),
    
]
