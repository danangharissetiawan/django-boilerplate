from .base import *

DEBUG = True

MIDDLEWARE += (
    'livereload.middleware.LiveReloadScript',
)
INSTALLED_APPS += [
    'livereload',
]