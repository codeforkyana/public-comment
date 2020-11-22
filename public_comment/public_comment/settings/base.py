"""
Django settings for renters' rights project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _


def get_env_variable(var_name, default=None):
    """Get the environment variable or return exception.

    Args:
      var_name: the name of the the environment variable to read.
      default: the value to return if the environment variable doesn't exit.

    Returns: the environment variable value, or the default value.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        if default:
            return default
        raise ImproperlyConfigured(f"Set the {var_name} environment variable")


def str_to_bool(value):
    str_value = str(value)
    true = str_value.lower() in ("yes", "true", "t", "1")
    false = str_value.lower() in ("no", "false", "f", "0")
    if true or false:
        return true or not false
    raise Exception("Bad string boolean value")


def str_to_int(value):
    return value if isinstance(value, int) else int(value)


SITE_NAME = get_env_variable("SITE_NAME", "KY Voter")
SITE_URL = get_env_variable("SITE_URL", "https://landlord/")
SITE_ID = 1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "7a9+m*y!4!951^c1ocyzp)bs51b(2*vc_==qh3^s%yx-ie*!@#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "bootstrap4",
    "django_tables2",
    "django_filters",
    "django_bootstrap_breadcrumbs",
    "localflavor",
    "modeltranslation",
    "maintenance_mode",
    "organizations",
    "comments",
    "sass_processor",
    "django_celery_results",
    "markdownx",
    "active_link",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    "csp.middleware.CSPMiddleware",
    "lib.middleware.TurbolinksMiddleware",
    "lib.middleware.OrganizationMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
]

ROOT_URLCONF = "public_comment.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
        "APP_DIRS": True,
    }
]

WSGI_APPLICATION = "public_comment.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "public_comment",
        "USER": "postgres",
        "PASSWORD": "pass",
        "HOST": "db",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    "sass_processor.finders.CssFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = "/s/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

LOCALE_PATHS = [os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "locale"))]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django": {"handlers": ["console"], "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"), "propagate": True},
        "django.request": {"handlers": ["console"], "level": os.getenv("DJANGO_REQUEST_LOG_LEVEL", "INFO"), "propagate": False},
        "comments": {"handlers": ["console"], "level": os.getenv("LOG_LEVEL", "INFO")},
        "lib": {"handlers": ["console"], "level": os.getenv("LOG_LEVEL", "INFO")},
    },
}

PHONENUMBER_DB_FORMAT = "E164"  # Twilio uses this format
PHONENUMBER_DEFAULT_REGION = "US"
PHONENUMBER_DEFAULT_FORMAT = "NATIONAL"

CACHE_TIMEOUT = get_env_variable("CACHE_TIMEOUT", 86400)
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache", "TIMEOUT": CACHE_TIMEOUT}}

# APP SETTINGS
LANGUAGES = [("es", _("Spanish")), ("en", _("English"))]

AUTH_USER_MODEL = "organizations.User"

CELERY_BROKER_URL = get_env_variable("REDISCLOUD_URL")
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_CACHE_BACKEND = "default"

AWS_S3_ENDPOINT_URL = None
AWS_S3_CUSTOM_DOMAIN = None
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID", "INVALID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY", "INVALID")
AWS_UPLOAD_BUCKET_NAME = get_env_variable("AWS_UPLOAD_BUCKET_NAME", "public-comment-uploads-test")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME", "public-comment-test")
AWS_S3_MAX_MEMORY_SIZE = 10485760  # 10 MB in bytes

BREADCRUMBS_TEMPLATE = "django_bootstrap_breadcrumbs/bootstrap4.html"

SHORT_DATETIME_FORMAT = "N j, Y, P T"
DATETIME_FORMAT = "N j, Y, P T"

LOGIN_URL = "/account/sign-in/"
LOGIN_REDIRECT_URL = "/"

TABLE_PAGE_SIZE = 50

# Content security policy settings
CSP_DEFAULT_SRC = ["'self'", "code.jquery.com", "cdn.jsdelivr.net", "stackpath.bootstrapcdn.com", "cdnjs.cloudflare.com"]
CSP_IMG_SRC = ["*"]
CSP_FRAME_SRC = ["'self'"]


DEFAULT_FROM_EMAIL = get_env_variable("DEFAULT_FROM_EMAIL", "webmaster@localhost")
