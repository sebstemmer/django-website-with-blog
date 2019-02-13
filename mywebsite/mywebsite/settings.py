import sys


# production: IN_DEVELOPMENT == False, development: IN_DEVELOPMENT == True
IN_DEVELOPMENT = True


# path to environment settings in development
ENV_SETTINGS_PATH_DEV = '/home/sebastian/my_data/Freelancer/sebastian-stemmer.com/internals/env_settings/'


# path to environment settings in production
ENV_SETTINGS_PATH_PROD = '/var/www/other/env_settings/'


# add environment settings to path
if IN_DEVELOPMENT:
    sys.path.append(ENV_SETTINGS_PATH_DEV)
else:
    sys.path.append(ENV_SETTINGS_PATH_PROD)


# import environment settings
import env_settings


# import development settings or production settings
if IN_DEVELOPMENT:
    from mywebsite.settings_dev import *
else:
    from mywebsite.settings_prod import *


# secret key
SECRET_KEY = env_settings.SECRET_KEY


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # start my own apps
    'mainpage.apps.MainpageConfig',
    'techblog.apps.TechblogConfig',
    # end my own apps
    # start wagtail apps
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    # end wagtail apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # start wagtail middleware
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    # end wagtail middleware
]

ROOT_URLCONF = 'mywebsite.urls'

#PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
                'mainpage.context_processor.ga',
                'mainpage.context_processor.private_data'
            ],
        },
    },
]

WSGI_APPLICATION = 'mywebsite.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_TZ = True


# static files
STATIC_URL = '/static/'


# media files
MEDIA_URL = '/media/'


# wagtail
WAGTAIL_SITE_NAME = 'My Example Site'


# private data
PRIVATE_DATA_STREET = env_settings.PRIVATE_DATA_STREET
PRIVATE_DATA_PHONE = env_settings.PRIVATE_DATA_PHONE
