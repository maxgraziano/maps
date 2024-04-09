import os
import datetime
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!7$l@$thnj@q-txtptk557nvgsc&17srn=7b7yh8)@*_p^ub8s'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    #'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'rest_framework',
    'rest_framework.authtoken', 
    'directory',
    'phonenumber_field',
    'address',
    'django_extensions',
    'corsheaders',
    'pytest',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#CORS_ORIGIN_ALLOW_ALL = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.yahoo.com' #'smtppro.zohopro.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'laredotornado@yahoo.com' #str(os.getenv('EMAIL_USER'))
EMAIL_HOST_PASSWORD = 'uspkrcwuilknrydb' # str(os.getenv('EMAIL_PASSWORD'))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dev.chicommons.coop', 'prod.chicommons.coop', 'map.chicommons.coop', EMAIL_HOST]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000', 'http://localhost:3001', 'http://127.0.0.1:3000', 'http://127.0.0.1:3001'
]

CORS_EXPOSE_HEADERS = [
    'Refresh-Token', 'Content-Type', 'Authorization', 'X-CSRFToken'
]
#CSRF_COOKIE_NAME = "csrftokennnnnn"
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ['localhost', '127.0.0.1']

ROOT_URLCONF = 'directory.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'directory.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/api/v1/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Configuration for phone numbers.
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'US'

LOGOUT_PATH = 'logout'

#AUTH_USER_MODEL = 'user.User'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
#     'DEFAULT_PERMISSION_CLASSES': [
#          'rest_framework.permissions.AllowAny',
#          #'rest_framework.permissions.IsAuthenticated',
#          #'rest_framework.permissions.IsAuthenticated',
#          #'rest_framework.permissions.IsAdminUser',
#          ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
#         #'directory.authentication.ExpiringTokenAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#        'rest_framework.authentication.SessionAuthentication',
#         #'rest_framework.authentication.BasicAuthentication',
    )
}

TOKEN_EXPIRED_AFTER_SECONDS = 86400

SECRET_KEY = 'This is a very long and secure secret key'


APPEND_SLASH=False

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ChiCommons Maps API',
    'VERSION': '1.0.0',
    # Other settings...
}