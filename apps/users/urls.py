from django.urls import path
from . import views

app_name = 'users' # routing for this app only

urlpatterns = [
    path('', views.index, name='users'),
    path('profile', views.profile, name='profile'),
]