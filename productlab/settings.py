import os
from pathlib import Path
from split_settings.tools import include


include(
    'components/auth_password_validators.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/databases.py',
) 


DEBUG = True
ALLOWED_HOSTS = []


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-)+*jr^)zrmt^@7287rx2p$y6#3^e!e&mu77l+!w@*4*p509ggg'
ROOT_URLCONF = 'productlab.urls'
WSGI_APPLICATION = 'productlab.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
