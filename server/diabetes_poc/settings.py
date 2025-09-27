import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "core",
    "quotas",
    "consent",
    "configurator",
    "runtime_engine",
    "submission",
    "clinical",
    "orchestrator",
    "extensions",
    "policies",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # CSRF kept enabled, but our API views will be csrf_exempt for simplicity
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.TenantContextMiddleware",
    "policies.middleware.ClaimsMiddleware",
    "consent.audit_middleware.AuditMiddleware",
]

ROOT_URLCONF = "diabetes_poc.urls"

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

WSGI_APPLICATION = "diabetes_poc.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Switchable to MySQL: set env DB_URL like mysql://user:pass@host:port/dbname
import os
DB_URL = os.environ.get("DB_URL")
if DB_URL and DB_URL.startswith("mysql://"):
    import urllib.parse as up
    up.uses_netloc.append("mysql")
    url = up.urlparse(DB_URL)
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.mysql",
        "NAME": url.path[1:],
        "USER": url.username,
        "PASSWORD": url.password or "",
        "HOST": url.hostname,
        "PORT": url.port or "3306",
        "OPTIONS": {"charset": "utf8mb4"},
    }

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}

# CORS settings for frontend-backend communication
CORS_ALLOWED_ORIGINS = [
    "https://your-netlify-app.netlify.app",  # Replace with your actual Netlify URL
    "http://localhost:5173",  # For local development
    "http://127.0.0.1:5173",  # For local development
]

# Allow all origins for development (remove in production)
CORS_ALLOW_ALL_ORIGINS = True

# Allow credentials to be included in CORS requests
CORS_ALLOW_CREDENTIALS = True

# Allow all headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-tenant',
    'x-roles',
    'x-departments',
    'idempotency-key',
]

# Allow all methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]