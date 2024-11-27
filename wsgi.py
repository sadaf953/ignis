import os
import sys

# Add your project directory to the sys.path
path = '/home/mahvishsadaf/eventbrite'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'eventbrite.settings'

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
