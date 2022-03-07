from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'documents' # routing for this app only

router = DefaultRouter()
router.register(r"documents", views.DocumentViewSet, "documents")


urlpatterns = [
    path("", include(router.urls)),
    # path('', views.index, name='documents'),
    # path('add', views.add, name='add'),
    # path('edit', views.edit, name='edit'),
    # path('delete', views.delete, name='delete'),
]