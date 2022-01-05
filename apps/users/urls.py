from django.urls import path, include
from .views import LoginView, LogoutView, SignUpView

urlpatterns = [
    # Auth views
    path('user/login/', LoginView.as_view(), name='auth_login'),
    path('user/logout/', LogoutView.as_view(), name='auth_logout'),
    path('user/signup/', SignUpView.as_view(), name='auth_signup'),
    path('user/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]