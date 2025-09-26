import os, dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY", "dev-not-secret")
DEBUG = os.environ.get("DEBUG", "False") == "True"

# SECRET_KEY = "dev-secret-key"
# DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
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

ROOT_URLCONF = "server.urls"

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

WSGI_APPLICATION = "server.wsgi.application"

# Postgres via DATABASE_URL
DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL", conn_max_age=600, ssl_require=True
    )
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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}


# CORS: pick one approach
CORS_ALLOWED_ORIGINS = [
    "https://your-site.netlify.app",
    "https://your-custom-domain.com",
]
# (For local dev only you might temporarily use CORS_ALLOW_ALL_ORIGINS=True)
# See package docs for options.  # :contentReference[oaicite:2]{index=2}

# Static files (admin, etc.)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


