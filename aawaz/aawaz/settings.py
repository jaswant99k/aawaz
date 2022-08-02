"""
Django settings for aawaz project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%gsunmkk+e$(aa3fo3a27(*x=4n5kv%go%7&yvsw=@^51#gpi8'

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
    'rest_framework',
    'user_management',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'admin_panel',
    'import_export',
    'tags',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'aawaz.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]


WSGI_APPLICATION = 'aawaz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIALACCOUNT_PROVIDERS = {
 'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
           'access_type': 'online',
        }
    }
}

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False



REST_USE_JWT = True



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True, # IMPORTANT
    'BLACKLIST_AFTER_ROTATION': True, # IMPORTANT
    'UPDATE_LAST_LOGIN': True,
}


FIREBASE_AUTH = {
    'FIREBASE_CREDENTIALS': {
        "type": "service_account",
        "project_id": "awaazproject-34fb8",
        "private_key_id": "d5122cf387b5b4a6714d6100700a66cbfa864f1c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDAXz54VrOBwtDN\nAKk8CaBc+9N8g/ZEk4uoFGz54I7ygg6ld2TkRoyyEFPad5SrEC3ig4xplC/lRwDX\nW/bYZE7magIEehTUCMlA0/rrNap12UGPm7iwQ667YopvHQUIY/yiCQOCG2k/SJHx\nFyQx+wuzhSzLTycpy+YGtAWFzecyOlu+u5xip4EablUUcgTbhCDaFJxHlCXh1wh7\nVW/aWIyWPK4kT3EIBvM6O+33dq/hVMvV4B8ziVVvsysbT1DhI7c3xjWmube7eGGC\npvvd2FzoerMCLfR51xmm1y/BCf6tL7xAv4I9rxTmIAv4+yemg2Jt/t/+BagoFm2G\neia4q7s3AgMBAAECggEARP8EJ2IlYOGQRS67BBsJxr/Vgv/LiJ4IxYCJ83dcndMS\n0LsJVyyMkuLzSFSCYHZdlrQK3OU25nt4bEWCO+uCNvcHgTaOGNyL3jIJeWoWmM0S\nzCCUdbfYyEGYGDEm2HMQLceg1/3f2kA7g+aCZ2C8uicGQWdCyyVj+7x+jJakmOkf\n3ed2tH9LiONsPeEG1KRkW6SjOSmdudmy/iO7uVM1ACnux0z7Sis/PJYIja89d+UR\nDnAPYtGfLtE1TOKOaEOTA5feUT4Ai11CCiE26T8/mynP4pAPJk4eLu0utVzkF886\nLPDndXmcSnWscNE7cdKzmtZXZMYAWD5k1+5pgWVUQQKBgQD9bRjKMkU6uS17Ebp2\n6enY7hCzNIcghUu23xLEkqcfzgUosbidutiaylBCCSgp50Gu/NY4IBHI+GG7IwHE\nnswiCTswcs5tWvMQsI7JpiFyrgDbqYsCz5SoQgYU2lpRiNX2qNTsPkd2aaWEec2z\nAZy7ZzbuHvl1dKWSr4HoHc/QQQKBgQDCU2hcr4l/rmaSR1xI+AJ3A7hAbEcWf7vs\nAQF7aGC+7IdG9ogYID58rzo4z1cZMKCs4dOV2g38rAbQ4hIDncc9iiCYAfxLN5P0\nUCwVMuS61j8Pw2nDej+xbWfoIynK/J3XWBJxYLXTL/a80GmC9x22iPI7eMxJuNRO\nQRhNl9atdwKBgQClFCWrwCc8Y1du7VNrFl/PgPO76CGFW47AZnrRNT5MB2Vw5qN9\nizKBUfwJp/FTqmIs3GGmWa18Hd97iQgjzdTm7uBxZLd2oGHoozm/vMnY6+N/Muds\nQ09wcuGHP9zJc7r8W2mnIcJnLdY1fyowyoIPyOINJnwUuJEKBe03CARQgQKBgQCp\nhcHBOZElxarNaVtkfJcJ5EDUUqEhS4VQuP/l/ISJiiXpDiBji513gBW2gYpl+znw\nF4FRdMxG5Ht9tfopFXc+hEUy1miV5YI428fZJnDLXSPeSIb3dKojymGe7S4EWqQH\nvFk6dzenaGxDAz1IdvOAza8jmpn8pjTvn3HoHtG0uQKBgQDaWKdcWl1jzWEy57II\nJziNPfFu+B3QKveWcn1gYuiqw1ny4BMi0ffQnMPzVsBdk+Rvkh3u9YBJPLOAnmme\nQfEiN8C6nZbgLfzEwfLjivhYumkTM5aWrpMNx7o8ghYctMtEInZYYvGfpk2X/mmQ\nD/XQxBxCIc69ZMkR3DhhLe7HJg==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-iho5b@awaazproject-34fb8.iam.gserviceaccount.com",
        "client_id": "116536491936065302582",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-iho5b%40awaazproject-34fb8.iam.gserviceaccount.com"
    }
}
#CORS_ORIGIN_ALLOW_ALL = True 
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        #'dj_rest_auth.utils.JWTCookieAuthentication',
        #'firebase_auth.authentication.FirebaseAuthentication',
        'rest_framework_firebase.authentication.FirebaseAuthentication',
    ]
}
