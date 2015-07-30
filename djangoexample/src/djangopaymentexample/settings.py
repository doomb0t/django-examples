"""
Django settings for djangopaymentexample project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

EMAIL_HOST = 'smtp.gmail.cpm'
EMAIL_HOST_USER = 'iwizardpdx@gmail.com'
EMAIL_HOST_PASSWORD = 'SUPER SECRET'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!bjs9#*dew=&srz8p%3_6u!c!+vg1z$hik^ci+sez#+g&03h*y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'profiles',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'stripe',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'djangopaymentexample.urls'

WSGI_APPLICATION = 'djangopaymentexample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# template directory path
TEMPLATE_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),)

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static", "static"),)   
    
CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "django.core.context_processors.csrf",
        )

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
        )

SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "My subject: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION  = True 
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


#media
