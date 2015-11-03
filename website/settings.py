import os
from os.path import dirname, join

ROOT = os.path.dirname(dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# DATABASES = {
#     'default': {
#         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'ENGINE': 'django.db.backends.sqlite3',
#         # Or path to database file if using sqlite3.
#         'NAME': join(ROOT, 'database.sqlite3'),
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         # Set to empty string for localhost. Not used with sqlite3.
#         'HOST': '',
#         # Set to empty string for default. Not used with sqlite3.
#         'PORT': '',
#     }
# }

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'sql695262',                    
    'USER': 'sql695262',                    
    'PASSWORD': 'aR9*yK8*',                
    'HOST': 'sql6.freemysqlhosting.net',                 
    'PORT': '3306',                     
    }
}


TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '9n&amp;8h$h$a@gr)$!&amp;2=g7=t=a)_d#^5ex1zd_!!r)fuw7@xnv!+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'website.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'website.wsgi.application'

TEMPLATE_DIRS = (
    join(ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_ace',
    'codegen',
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'