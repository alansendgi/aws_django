import os
import sys

path = '/srv/project/aws_django'
if path not in sys.path:
    sys.path.insert(0, '/srv/project/aws_django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'aws_django.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
