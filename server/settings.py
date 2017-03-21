import os
import sys
import tempfile
# BASE_DIR = tempfile.mkdtemp()
# BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),'where')
os.environ.setdefault("aristotlemdr__BASE_DIR", tempfile.mkdtemp())

from aristotle_mdr.required_settings import *

DEBUG = True # Force us to have the static files served for us

sys.path.insert(1, BASE_DIR)

SECRET_KEY = 'inara+i-am-the-documentation-server-never-for-production'
ALLOWED_HOSTS=['*']
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'

skip_migrations = True

from aristotle_mdr.tests.settings.templates.db.sqlite import DATABASES

HAYSTACK_CONNECTIONS = {
    'default': {
        #'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'aristotle_mdr.contrib.search_backends.facetted_whoosh.FixedWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}


MIDDLEWARE_CLASSES = (
    'insecure.DisableCSRF',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'aristotle_mdr.contrib.redirect.middleware.RedirectMiddleware',
)

if skip_migrations:  # pragma: no cover
    print("Skipping migrations")
    class DisableMigrations(object):
    
        def __contains__(self, item):
            return True
    
        def __getitem__(self, item):
            return "notmigrations"
    
    MIGRATION_MODULES = DisableMigrations()


INSTALLED_APPS = (
    # The good stuff
    'aristotle_mdr.contrib.self_publish',
    'aristotle_mdr.contrib.links',
) + INSTALLED_APPS


# https://docs.djangoproject.com/en/1.10/topics/testing/overview/#speeding-up-the-tests
# We do a lot of user log in testing, this should speed stuff up.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] = ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] + ['aristotle_mdr_links']
ARISTOTLE_SETTINGS['SITE_NAME'] = "My Registry"
ARISTOTLE_SETTINGS['SITE_INTRO'] = "Use Aristotle Metadata Registry to search for metadata..."

ARISTOTLE_SETTINGS['BULK_ACTIONS'].update({
    'quick_pdf_download':'aristotle_mdr.forms.bulk_actions.QuickPDFDownloadForm',
    'add_slots': 'aristotle_mdr.contrib.slots.forms.BulkAssignSlotsForm',
})

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__),'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'aristotle_mdr.context_processors.settings',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG
        },
    },
]
