from django.urls import path
from shoedata import views

urlpatterns = [
    path('', views.index, name='home')
    ]
