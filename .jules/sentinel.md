# Sentinel Journal

## Findings

* **ApiPermission AttributeError**: In `app/eventyay/api/permissions.py`, `ApiPermission._has_permission` blindly called `request.auth.has_endpoint_permission`. Because `request.auth` could be `Device`, `OAuthAccessToken`, `TeamAPIToken`, or standard `User` object, and only `UserApiToken` implements this method, it would crash via an `AttributeError`. This was particularly impactful because any API endpoint utilizing `ApiPermission` would return a 500 status when authenticated by any mechanism other than a `UserApiToken`. This is a production crash scenario due to missing polymorphism / interface contracts.
