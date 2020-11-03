from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('auth_log', views.auth_log), 
    path('success', views.success),
    path('logout', views.logout),
]