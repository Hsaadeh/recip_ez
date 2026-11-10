import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG")
if DEBUG == "False":
    DEBUG = False
else:
    DEBUG = True


USE_PRODUCTION_DB = os.getenv("USE_PRODUCTION_DB")
if USE_PRODUCTION_DB == "True":
    USE_PRODUCTION_DB = True
else:
    USE_PRODUCTION_DB = False


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djmoney',
    'profiles',
    'list_manager',
    'recipe_manager',
    'assistant',
    'tailwind',
    'theme',
    'django_cleanup.apps.CleanupConfig',
]

AUTH_USER_MODEL = "profiles.CustomUser"

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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'theme.context_processor.template_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

if USE_PRODUCTION_DB:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = os.getenv("STATIC_URL")
# STATIC_ROOT = os.path.dirname(BASE_DIR) + os.getenv("STATIC_ROOT")
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media Files
MEDIA_URL = os.getenv("MEDIA_URL")
MEDIA_ROOT = os.path.dirname(BASE_DIR) + os.getenv("MEDIA_ROOT")
MEDIAFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), os.getenv("MEDIAFILES_DIRS"))
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
WHITENOISE_ROOT = os.path.join(BASE_DIR, os.getenv("WHITENOISE_ROOT"))

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}

TAILWIND_APP_NAME = 'theme'
TAILWIND_CSS_PATH = 'css/dist/styles.css'

NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'

DEFAULT_VIEW = "view_recipes"
NOT_FOUND_VIEW = "view_not_found"

HTTP_PROTOCOL=os.getenv("HTTP_PROTOCOL")
SITE_URL=os.getenv("SITE_URL")

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION=os.getenv("AWS_REGION")
AWS_MODEL_ID=os.getenv("AWS_MODEL_ID")
AWS_KNOWLEDGE_BASE_ID=os.getenv("AWS_KNOWLEDGE_BASE_ID")
