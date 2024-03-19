from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true" ###

# GW_WKHTML = "/usr/local/bin/wkhtmltopdf"
# CSS1_WKHTML = '/home/gili/Python/CompanyApp/MyApp/static/printPDF/jquery-1.10.2.min.js'
# CSS2_WKHTML = '/home/gili/Python/CompanyApp/MyApp/static/printPDF/bootstrap.min.css'
# CSS3_WKHTML = '/home/gili/Python/CompanyApp/MyApp/static/printPDF/bootstrap.bundle.min.js'
# LOGO_CAP = '/home/gili/Python/CompanyApp/MyApp/static/pt_img/logo.jpg'
# TTD_CAP = '/home/gili/Python/CompanyApp/MyApp/static/pt_img/ttdCAP1.png'
# LOGO_SA = ''
# TTD_SA = '/home/gili/Python/CompanyApp/MyApp/static/pt_img/ttdSA.jpg'
# LOGO_PYDEVL = '/home/gili/Python/CompanyApp/MyApp/static/pt_img/PyDevL.jpg'
# TTD_PYDEVL = '/home/gili/Python/CompanyApp/MyApp/static/pt_img/my_ttd_no_bg.png'

GW_WKHTML = "/home/cannindica/wkthml-install/usr/local/bin/wkhtmltopdf"
CSS1_WKHTML = '/home/cannindica/CAP/static/printPDF/jquery-1.10.2.min.js'
CSS2_WKHTML = '/home/cannindica/CAP/static/printPDF/bootstrap.min.css'
CSS3_WKHTML = '/home/cannindica/CAP/static/printPDF/bootstrap.bundle.min.js'
LOGO_CAP = '/home/cannindica/CAP/static/pt_img/logo.jpg'
TTD_CAP = '/home/cannindica/CAP/static/pt_img/ttdCAP1.png'
LOGO_SA = ''
TTD_SA = '/home/cannindica/CAP/static/pt_img/ttdSA.jpg'
LOGO_PYDEVL = '/home/cannindica/CAP/static/pt_img/PyDevL.jpg'
TTD_PYDEVL = '/home/cannindica/CAP/static/pt_img/my_ttd_no_bg.png'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kc3c6&-2az_eibyhc8!a!zi@5ra$#(5)hok_lq#ym$m-^lt2sb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'django_cleanup',
    'MainApp',
    'INV',
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

ROOT_URLCONF = 'MyApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'MyApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True

USE_L10N = False
USE_DECIMAL_SEPARATOR = True
DECIMAL_SEPARATOR = ","
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = "."


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'templates/static',
]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'MainApp:login'
LOGOUT_URL = 'MainApp:logout'
LOGIN_REDIRECT_URL = 'MainApp:home'