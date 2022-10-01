from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9s-@n3o_j8hb%0y1o5ewus2$)5(bwu_6pm3@_n2!98q8=(*4v0'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wordToImage_db',
        'HOST': 'localhost',
        'USER': 'wordToImage_app',
        'PASSWORD': '1234'
    }
}
