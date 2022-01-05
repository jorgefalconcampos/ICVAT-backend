"""
Django settings for backend project.
Generated by 'django-admin startproject' using Django 3.2.9.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os, sys
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.

PROJECT_DIR = Path(__file__).resolve().parent # ===> PROJECT FOLDER 
BASE_DIR = PROJECT_DIR.parent # ===> ROOT FOLDER




# Templates directories
TEMPLATES_DIR = PROJECT_DIR / 'templates' # ===> project templates



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', default="django-insecure-cd8um+tpv=t#0kb)%t7*g$j81g4+ju(bcg8fu+1d)ej0muzvb^")


# SECURITY WARNING: don't run with debug turned on in production!
IS_LIVE = 'RENDER' in os.environ

if IS_LIVE:
    DEBUG = False
    # print("\n Running live!! \n\n")
else:
    DEBUG = True
    # print("\n Running in debug mode \n\n")


ALLOWED_HOSTS = ['*']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME') #this env variable is automatically set by Render

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)




sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))




# Application definition

INSTALLED_APPS = [
    # custom apps
    'categories',
    'dashboard',
    'documents',
    'users',
    # third-party apps
    'rest_framework',
    'corsheaders',
    'django_rest_passwordreset',
    'django_summernote',
    # built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Cors settings
CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://localhost:8080", "http://localhost:8080", "http://localhost:8081"]
CORS_ALLOW_CREDENTIALS = True


# Django Rest Framework (DRF) settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}



ROOT_URLCONF = 'backend.urls'

AUTH_USER_MODEL="users.User"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATES_DIR ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if IS_LIVE:
    DATABASES = {
        'default': dj_database_url.config(
            # Feel free to alter this value to suit your needs.
            default=os.environ.get('POSTGRES_EXTERNAL_CONNECTION_URL'),
            # default='postgresql://postgres:postgres@localhost:5432/mysite',
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': BASE_DIR / 'db.sqlite3',
            'NAME': str(os.path.join(BASE_DIR, 'db.sqlite3')),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'




# Following settings only make sense on production and may break development environments.
if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'