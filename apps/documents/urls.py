from django.urls import path
from . import views

app_name = 'documents' # routing for this app only

urlpatterns = [
    path('', views.index, name='documents'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
]