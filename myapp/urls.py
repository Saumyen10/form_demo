from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.new, name='new'),
    path('new.html', views.new, name='new'),
    
]
