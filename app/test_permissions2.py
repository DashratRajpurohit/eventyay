import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventyay.config.settings")
django.setup()

from eventyay.api.permissions import ApiPermission
from rest_framework.request import Request
from django.http import HttpRequest
from eventyay.base.models import Event, Organizer, User
from eventyay.api.models import OAuthAccessToken, OAuthApplication
from django.test import RequestFactory

factory = RequestFactory()
request = factory.get('/')
request.user = User()
request.auth = OAuthAccessToken()
request.auth.application = OAuthApplication()
# Trying to emulate the DRF context
print("OAuth grant without events attribute:")
try:
    print(request.auth.events.all())
except Exception as e:
    print("Error:", e)
