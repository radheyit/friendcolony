"""
WSGI config for friendcolony project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
import sys
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
print ("PROJECT_PATH: ", PROJECT_PATH)
ve = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
Virtual_Environment = os.path.join(ve, "ve/lib/python3.4/site-packages")
print("Virtual_Environment: ", Virtual_Environment)

sys.path.append("/home/nirmalit/python_workspace/friendcolony")
sys.path.append("/home/nirmalit/python_workspace/ve/lib/python3.4/site-packages")

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friendcolony.settings")
application = get_wsgi_application()
