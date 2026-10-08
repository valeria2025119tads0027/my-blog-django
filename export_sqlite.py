import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.conf import settings
settings.DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}
from django.core.management import call_command
call_command('dumpdata', indent=2, output='mysite_data.json')
