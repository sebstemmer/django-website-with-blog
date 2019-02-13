import os
import env_settings

# debug variable
DEBUG = True


# send emails to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# admin
ADMIN_ENABLED = True


# media
MEDIA_ROOT = os.path.join(env_settings.DEV_DIR, 'media/')


# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(env_settings.DEV_DIR, 'db.sqlite3'),
    }
}