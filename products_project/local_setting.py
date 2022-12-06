# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6esq18ev!s(1ie8sdl8=fajqs2!-t5fi%5_i&$(yv$gb_g59%%'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'R00ster39!'
    }
}
