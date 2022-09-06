from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'categories' 

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, "categories")

urlpatterns = [
    path("", include(router.urls)),
    # path('test-static/', views.static, name='static'),

    # path('categories/', views.list_categories ),
    # path('categories/', views.CategoryList.as_view()),
    # path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    # # path('', views.categories, name='categories'),
    # path('add', views.add, name='add'),
    # path('edit', views.edit, name='edit'),
    # path('delete', views.delete, name='delete'),
]