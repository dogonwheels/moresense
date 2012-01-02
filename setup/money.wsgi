import os, sys

activate_this = "/home/money/env/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, "/home/money/site")
sys.path.insert(0, "/home/money/site/moresense")
os.environ['DJANGO_SETTINGS_MODULE'] = 'moresense.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
