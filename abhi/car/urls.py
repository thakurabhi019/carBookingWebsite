from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('book',views.car),
    path('show',views.show),
    path('show/<str:pk>/',views.show)
]