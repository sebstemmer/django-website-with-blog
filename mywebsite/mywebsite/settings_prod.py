import os
import env_settings


# debug variable
DEBUG = False


# allowed hosts
ALLOWED_HOSTS = [
    'www.sebastian-stemmer.com',
    'sebastian-stemmer.com',
]


# static files
STATIC_ROOT = os.path.join(env_settings.PROD_DIR, 'static/')


# session and CSRF cookie only send via https
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# prevent xss attack
SECURE_BROWSER_XSS_FILTER = True


# x frame options
X_FRAME_OPTIONS = 'DENY'


# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(env_settings.PROD_DIR, 'logs/debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# admin
ADMIN_ENABLED = False


# media
MEDIA_ROOT = os.path.join(env_settings.PROD_DIR, 'media/')


# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env_settings.DATABASE_NAME,
        'USER': env_settings.DATABASE_USER,
        'PASSWORD': env_settings.DATABASE_PW,
        'HOST': 'localhost',
        'PORT': '',
     }
}


# google analytics
GA_TRACKING_ID = env_settings.GA_TRACKING_ID