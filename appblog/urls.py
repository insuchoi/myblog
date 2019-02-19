from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>' , views.detail, name='detail'),
]