import os
from .common import *
import dj_database_url
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["vfls.herokuapp.com", "f-links-shortener.herokuapp.com"]

DATABASES = {
    'default': dj_database_url.config()
}
