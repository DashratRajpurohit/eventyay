import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventyay.config.settings")
django.setup()

from eventyay.api.permissions import ApiPermission
from rest_framework.request import Request
from django.http import HttpRequest
from eventyay.base.models import Event, Organizer, User, Device, TeamAPIToken
from eventyay.base.models.auth_token import UserApiToken
from eventyay.api.models import OAuthAccessToken, OAuthApplication

d = OAuthAccessToken()
try:
    print("OAuthAccessToken events:", getattr(d, 'events', None))
    print("OAuthAccessToken events.all():", d.events.all() if hasattr(d, 'events') else 'N/A')
except Exception as e:
    print("OAuthAccessToken events error:", e)
