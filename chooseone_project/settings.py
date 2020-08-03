"""
Django settings for chooseone_project project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['chooseone.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'social_django',
    'django_extensions',
    'rosetta',

    # Local
    'home.apps.HomeConfig',
    'contents.apps.ContentsConfig',
]

SITE_ID=1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chooseone_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'chooseone_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

from django.utils.translation import gettext_lazy as _
LANGUAGE = (
    ('en', _('English')),
    ('ja', _('Japanese')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'),]
STATIC_ROOT=os.path.join(BASE_DIR, 'static/')
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


SITE_ID=1
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL='dashboard'
LOGIN_URL='login'
LOGOUT_URL='account_signup'
# ACCOUNT_LOGOUT_REDIRECT='dashboard'

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '1386651581532111' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '0ddb51c511fa2fcf7726308ecc4cb871' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '722704825746-dfh6sto2skudnb6gjsn4mbahn3h5eesm.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '9B4xwRklxzY_26rXEZziYXx_' # Google Consumer Secret


ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True


DEFAULT_FROM_EMAIL='admin@chooseone.com'


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

REDIS_HOST='docker.for.mac.localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# smile
# earth meal rinne
# love and wash
