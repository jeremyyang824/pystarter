import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 'gldwzgsm6)%kl8^i5eoy=*%sc0cxoif@xqye@x!47y#w*1!d7_')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,testserver').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (os.path.join(BASE_DIR, 'templates'),),
            'APP_DIRS': True
        },
    ),
    # STATICFILES_DIRS=(
    #     os.path.join(BASE_DIR, 'static'),
    # ),
    STATICFILES_FINDERS=(
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #'compressor.finders.CompressorFinder',
    ),
    STATIC_URL='/static/',
    # page dir
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    # output root dir
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
    # output static dir
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static')
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
