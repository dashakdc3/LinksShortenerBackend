from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-cd9!!l&l7-*lu*@a8xq_ux(p#hq(4@cbi)wp1dn9&4=&f9si(b'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '132465798'
    }
}
ALLOWED_HOSTS = ["*"]