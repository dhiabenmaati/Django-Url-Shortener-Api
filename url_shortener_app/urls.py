from django.contrib import admin
from django.urls import path
from url_shortener_app import views


urlpatterns = [
    
    path('all-links', views.urlList, name='urls'),
    path('create-link', views.urlCreate, name='create'),
    path('delete-link/<str:pk>/', views.urlDelete, name='delete'),
    path('redirect/<str:pk>/', views.urlRedirect, name='redirect'),
]