CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/cache',
        'TIMEOUT': 7140,
    }
}