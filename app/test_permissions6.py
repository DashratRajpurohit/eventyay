import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventyay.config.settings")
django.setup()

from eventyay.api.permissions import ApiPermission
from rest_framework.request import Request
from django.http import HttpRequest
from eventyay.base.models import Event, Organizer, User, Device, TeamAPIToken
from eventyay.api.models import OAuthAccessToken, OAuthApplication

def mock_request(auth):
    class RequestMock:
        def __init__(self, auth):
            self.auth = auth
            self.user = User()
            self.event = Event()
    return RequestMock(auth)

permission = ApiPermission()

try:
    print("Device Token test:")
    req = mock_request(Device())
    print("Has permission?", permission._has_permission(None, None, req))
except Exception as e:
    print("Device token test failed:", e)

try:
    print("Team Token test:")
    req = mock_request(TeamAPIToken())
    print("Has permission?", permission._has_permission(None, None, req))
except Exception as e:
    print("Team token test failed:", e)
