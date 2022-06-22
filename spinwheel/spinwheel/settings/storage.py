import os

from spinwheel.settings.settings import BASE_DIR


# Database

# Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'NAME': os.environ.get('DB_NAME', 'db'),
        'USER': os.environ.get('DB_USER', 'user'),
        'PASSWORD': os.environ.get('DB_PASS', '123'),
    }
}

# Static files

STATIC_URL = '/static/'
STATIC_ROOT = '/vol/web/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
