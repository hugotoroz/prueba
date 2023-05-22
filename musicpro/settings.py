"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from django.urls import reverse_lazy
#from transbank import webpay


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#&rohuqrmjzn@9nixi38!-+3p_*=klp%(8x)ngo-a4o0(n36=z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'basket',
    'django_countries',
    # 'account',
    'payment',
    'cuenta',
    'order',
    'rest_framework',
    'api',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'musicpro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.views.categories',
                'basket.context_processors.basket'
            ],
        },
    },
]

WSGI_APPLICATION = 'musicpro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prueba_mp2',
        'USER': 'hugo',
        'PASSWORD': '123',
        'HOST': '192.168.1.88',
        'PORT': '3306',
        'OPTIONS':{
            'init_command': 'SET default_storage_engine=INNODB',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media/')

   #Custom user Model
# AUTH_USER_MODEL = 'account.UserBase'
# LOGIN_REDIRECT_URL = '/account/dashboard'
# LOGIN_URL = '/account/login/'

# PASSWORD_RESET_TIMEOUT_DAYS = 3


# LOGIN_REDIRECT_URL = reverse_lazy('home.html')
# LOGOUT_REDIRECT_URL = reverse_lazy('home.html')

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'


# Stripe Payment
PUBLISHABLE_KEY = 'pk_test_51N8dRNDhCox3RGVY1ANKDbVMHf5pKALkRuOAdAssIkYXe5Fa6yxd0PYHTJjTKwQ4iwri616lGnRnq0IQQfDmmAMH005ZVIGUsj'
SECRET_KEY = 'sk_test_51N8dRNDhCox3RGVYeRbWn9ZjCW7FBwY5DsDBb0LTTdlVSTuGFd69KjhWuoruOXHdghJGWFh4nN7m1alN66ZLn51J00FzhebERf'
STRIPE_ENDPOINT_SECRET = 'whsec_55fe471ec073d0e19badc0d105dbd2b697b3a23d1d123626546cad66493442ef'
# stripe listen --forward-to localhost:8000/payment/webhook/

#Basket session id (Coock ie)
BASKET_SESSION_ID = 'basket'
