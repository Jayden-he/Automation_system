"""
Django settings for ops project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f=5d@qx=x0kr=0eeuwvjxi-xwzafttb^biemvvyy$m!2*d_xib'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.humanize',
    'account',
    'assets',
    'bootstrapform',
	'pagination',
	'ticket',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cmdb_v4.urls'

WSGI_APPLICATION = 'cmdb_v4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'cmdb_v4',
	'USER': 'django',
	'PASSWORD': 'django123.',
	'HOST': '127.0.0.1',
	'PORT': '3306',
	
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
	('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
	('img', os.path.join(STATIC_ROOT, 'img').replace('\\', '/')),
	('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
	('extra', os.path.join(STATIC_ROOT, 'extra').replace('\\', '/')),
	('bootstrap', os.path.join(STATIC_ROOT, 'bootstrap').replace('\\', '/')),
	('new', os.path.join(STATIC_ROOT, 'new').replace('\\', '/')),
	('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
	('ztree', os.path.join(STATIC_ROOT, 'ztree').replace('\\', '/')),
	('layer', os.path.join(STATIC_ROOT, 'layer').replace('\\', '/')),
	('external', os.path.join(STATIC_ROOT, 'external').replace('\\', '/')),
	('pdf', os.path.join(STATIC_ROOT, 'pdf').replace('\\', '/')),
	('lib', os.path.join(STATIC_ROOT, 'lib').replace('\\', '/')),
	('plugins', os.path.join(STATIC_ROOT, 'plugins').replace('\\', '/')),
	('md', os.path.join(STATIC_ROOT, 'md').replace('\\', '/')),
)








TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

LOGIN_URL='/account/login'
