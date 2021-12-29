from django.urls import path
from . import views

app_name = 'a12n' # routing for this app only

urlpatterns = [
    path('', views.index, name='a12n'),
]