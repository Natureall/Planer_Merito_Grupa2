from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-demo-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'panel_wsb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        'DIRS': [BASE_DIR / 'main' / 'templates'],
    },
]

WSGI_APPLICATION = 'panel_wsb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'



LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

'django_widget_tweaks',


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


JAZZMIN_SETTINGS = {
    "site_title": "WSB Admin",
    "site_header": "Panel Administracyjny",
    "site_logo": None,
    "site_logo_classes": "img-circle",
    "welcome_sign": "Witaj w Panelu Administracyjnym WSB",
    "copyright": "WSB",
    "topmenu_links": [
        {"name": "Strona Główna",  "url": "/", "permissions": ["auth.view_user"]},
    ],
    "use_google_fonts_cdn": True,
}




JAZZMIN_SETTINGS = {
    "site_title": "Administracja Django",
    "site_header": "Administracja Django",
    "site_brand": "Panel WSB",
    "welcome_sign": "Witaj w panelu administratora",
    "show_sidebar": True,
    "navigation_expanded": True,
    "apps": {
        "main": {
            "label": "Panel użytkownika",
            "icon": "fas fa-user-cog",
        },
    },
    "custom_links": {},
}
