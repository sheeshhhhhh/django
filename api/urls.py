from django.urls import path
from . import views

urlpatterns = [
    path('loginapi/', views.Login, name='login'),
]