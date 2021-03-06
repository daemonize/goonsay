# Import global settings to make it easier to extend settings. 
from django.conf.global_settings import *
# Import the project module to calculate directories relative to the module
# location.
import os
import goonsay

PROJECT_ROOT, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(goonsay.__file__))
)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME, 'static')

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

ROOT_URLCONF = 'goonsay.conf.urls'

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

PISTON_EMAIL_ERRORS = False

HAYSTACK_SITECONF = 'goonsay.conf.search'

HAYSTACK_SEARCH_ENGINE = 'whoosh'

HAYSTACK_WHOOSH_PATH = '/home/goonsay/whoosh/goonsay_index'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME, 'templates'),
)

CACHE_BACKEND = 'dummy:///'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'gatekeeper.middleware.GatekeeperMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'staticfiles.context_processors.static_url',
    'navbar.context_processors.navbars',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django_extensions',
    'staticfiles',
    'south',

    'gatekeeper',
    'navbar',
    'haystack',

    'goonsay.apps.goonsay',
    'goonsay.apps.search',
    'goonsay.apps.voting',
    'goonsay.apps.api',
)
