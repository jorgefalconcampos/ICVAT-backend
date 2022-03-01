from django.urls import path, include
# from .views import LoginView, LogoutView, SignUpView
from . import views

urlpatterns = [
    # Auth views
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('restric/', views.restricted),
]