
import os
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGIN_URL = reverse_lazy('apps.blog_auth:sesion')
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')


# SECURITY WARNING: keep the secret key used in production secret!
ENV_SECRET_KEY = os.getenv("SECRET_KEY")

SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'apps.post',
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'



NAME_DB = os.getenv("NAME_DB")
USER_DB = os.getenv("USER_MYSQL")
PASSWORD_DB =  os.getenv("PASSWORD_MYSQL")

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "NAME": NAME_DB,
        "USER": USER_DB,
        "PASSWORD": PASSWORD_DB,
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


# Password validation

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

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATICFILES_DIRS= os.path.join(os.path.dirname(BASE_DIR), 'static'),   #(os.path.join(os.path.dirname(BASE_DIR), 'static'),)

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media') #os.path.join(os.path.dirname(BASE_DIR), 'media')