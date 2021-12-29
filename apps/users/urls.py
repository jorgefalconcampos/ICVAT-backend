from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('profile', views.profile, name='profile'),
]