from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name= "home"),
    path('home.html', views.home, name = "home"),
    path('butterpaneer.html', views.butterpaneer, name = "butterpaneer")
    
]
