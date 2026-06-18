import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventyay.config.settings")
django.setup()

from eventyay.api.permissions import ApiPermission
from rest_framework.request import Request
from django.http import HttpRequest
from eventyay.base.models import Event, Organizer
from eventyay.api.models import OAuthAccessToken, OAuthApplication

print("Loaded")
