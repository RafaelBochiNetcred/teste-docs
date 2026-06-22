import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-test-docs"
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() in {
    "1",
    "true",
    "yes",
}
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    "drf_spectacular",
    "webhooks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Netcred API REST",
    "DESCRIPTION": (
        "Schema OpenAPI 3 gerado automaticamente com drf-spectacular para "
        "documentar endpoints REST consumidos por clientes e integradores. "
        "Esta primeira versao publica cobre o recurso de Webhooks e e renderizada "
        "com ReDoc."
    ),
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api",
    "PREPROCESSING_HOOKS": [
        "webhooks.schema_hooks.only_documented_endpoints",
    ],
    "COMPONENT_SPLIT_REQUEST": True,
    "SORT_OPERATIONS": False,
    "TAGS": [
        {
            "name": "Webhooks",
            "description": (
                "Gerenciamento das assinaturas usadas para receber notificacoes "
                "de eventos da plataforma Netcred.\n\n"
                "Uma assinatura define a URL do integrador, a empresa vinculada, "
                "os eventos que disparam notificacoes e a chave usada para assinar "
                "o payload quando necessario.\n\n"
                "Eventos suportados: "
                "`ANY`, `CHARGE_CREATE`, `CHARGE_UPDATE`, "
                "`CHARGE_VOID`, `TRANSACTION_CREATE`, `TRANSACTION_CAPTURE`, "
                "`TRANSACTION_EXPIRED`, `TRANSACTION_UPDATE`, `TRANSACTION_VOID`, "
                "`TRANSACTION_REFUND`, `TRANSACTION_DISPUTE`, "
                "`TRANSACTION_AUTHORIZE`, `PAYMENT_PROFILE_TOKENIZE`, "
                "`PAYMENT_PROFILE_UPDATE`, `PAYMENT_PROFILE_DELETE`, "
                "`PAYMENT_PROFILE_EXPIRING` e `WEBHOOK_PING`.\n\n"
                "Headers enviados pela Netcred ao chamar a URL do integrador: "
                "`Content-Type: application/json`, `User-Agent`, "
                "`X-Netcred-Event`, `X-Netcred-Delivery` e "
                "`X-Netcred-Signature` quando `secret_key` foi configurada."
            ),
        },
    ],
}
