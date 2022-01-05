from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('add', views.add, name='add'),
    path('test-static', views.static, name='static'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
]