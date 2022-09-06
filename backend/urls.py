"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404
# from rest_framework import routers

# -------------------#
#    Project URL'S   #
# -------------------#

# router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    path('api/', include('users.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('documents.urls')),
    path('api/', include('tags.urls')),
    
    # path('api/', include(router.urls)),
]


handler404 = 'backend.views.page_not_found_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)