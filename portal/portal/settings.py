import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
import ssl

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "import_export",
    "mptt",
    "django_python3_ldap",
    "django_select2",
    "accounts",
    "main",
    "phonebook",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portal.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

LANGUAGES = [
    ("ru", _("Russian")),
    ("kk", _("Kazakh")),
]

TIME_ZONE = "Asia/Almaty"

MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
MODELTRANSLATION_PREPOPULATE_LANGUAGE = "ru"

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# accounts
AUTH_USER_MODEL = "accounts.CustomUser"

# LDAP Configuration
LDAP_AUTH_URL = config("LDAP_AUTH_URL")
LDAP_AUTH_USE_TLS = True

LDAP_AUTH_TLS_VERSION = ssl.PROTOCOL_TLS
LDAP_AUTH_SEARCH_BASE = "DC=kmo,DC=kz"
LDAP_AUTH_OBJECT_CLASS = "organizationalPerson"
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
LDAP_AUTH_FORMAT_SEARCH_FILTERS = "django_python3_ldap.utils.format_search_filters"
LDAP_AUTH_FORMAT_USERNAME = (
    "django_python3_ldap.utils.format_username_active_directory_principal"
)
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "kmo.kz"
LDAP_AUTH_CONNECTION_USERNAME = config("LDAP_AUTH_CONNECTION_USERNAME")
LDAP_AUTH_CONNECTION_PASSWORD = config("LDAP_AUTH_CONNECTION_PASSWORD")
LDAP_AUTH_CONNECT_TIMEOUT = None
LDAP_AUTH_RECEIVE_TIMEOUT = None

AUTHENTICATION_BACKENDS = (
    "django_python3_ldap.auth.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)
