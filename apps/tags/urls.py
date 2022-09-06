from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'tags'

router = DefaultRouter()
router.register(r"tags", views.TagsViewSet, "tags")


urlpatterns = [
    path("", include(router.urls)),
]