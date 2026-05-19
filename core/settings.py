from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['web-production-405e6.up.railway.app', '127.0.0.1', 'localhost']

# ── CSRF Fix ──────────────────────────────────────────────
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-405e6.up.railway.app',
]


# Only enforce secure cookies on production, not locally
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# ── Jazzmin ───────────────────────────────────────────────
JAZZMIN_SETTINGS = {
    "site_title": "Rikhil Admin",
    "site_header": "Rikhil Portfolio",
    "site_brand": "Rikhil.dev",
    "welcome_sign": "Welcome back, Rikhil",
    "copyright": "Kakani Rikhil",
    "topmenu_links": [
        {"name": "View Portfolio", "url": "/", "new_window": True},
    ],
    "icons": {
        "auth":                     "fas fa-users-cog",
        "auth.user":                "fas fa-user",
        "auth.Group":               "fas fa-users",
        "portfolio.Profile":        "fas fa-id-card",
        "portfolio.Project":        "fas fa-code",
        "portfolio.Skill":          "fas fa-star",
        "portfolio.Experience":     "fas fa-briefcase",
        "portfolio.Education":      "fas fa-graduation-cap",
        "portfolio.Certification":  "fas fa-certificate",
    },
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "portfolio",
        "portfolio.Profile",
        "portfolio.Project",
        "portfolio.Skill",
        "portfolio.Experience",
        "portfolio.Education",
        "portfolio.Certification",
        "auth",
    ],
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text":   False,
    "brand_small_text":  False,
    "brand_colour":      False,
    "accent":            "accent-primary",
    "navbar":            "navbar-dark",
    "no_navbar_border":  True,
    "navbar_fixed":      True,
    "layout_boxed":      False,
    "footer_fixed":      False,
    "sidebar_fixed":     True,
    "sidebar":           "sidebar-dark-primary",
    "sidebar_nav_small_text":    False,
    "sidebar_disable_expand":    False,
    "sidebar_nav_child_indent":  True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style":  False,
    "sidebar_nav_flat_style":    False,
    "theme":             "darkly",
    "dark_mode_theme":   "darkly",
    "button_classes": {
        "primary":   "btn-primary",
        "secondary": "btn-secondary",
        "info":      "btn-outline-info",
        "warning":   "btn-warning",
        "danger":    "btn-danger",
        "success":   "btn-success",
    },
}

# ── Apps ──────────────────────────────────────────────────
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # staticfiles FIRST
    'cloudinary',
    'cloudinary_storage',          # cloudinary AFTER staticfiles
    'portfolio',
]

# ── Middleware ────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.context_processors.profile',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# ── Database ──────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ── Email ─────────────────────────────────────────────────
# IMPORTANT: move these to Railway environment variables!
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER', 'kakanirikhil7@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'fgcs nxbc tios hyxf')

# ── Password validation ───────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalisation ──────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_TZ        = True

# ── Static files ──────────────────────────────────────────
STATIC_URL        = '/static/'
STATICFILES_DIRS  = [os.path.join(BASE_DIR, 'portfolio/static')]
STATIC_ROOT       = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ── Media files → Cloudinary ──────────────────────────────
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key    = os.environ.get('CLOUDINARY_API_KEY'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET'),
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY'   : os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# New setting name for Django 4.2+
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",  # removed 'Manifest'
    },
}