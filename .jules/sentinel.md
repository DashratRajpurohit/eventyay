# Sentinel Discovery Journal

## Date: $(date +"%Y-%m-%d")

### DRF Authentication Interface Fragmentation
Discovered a critical vulnerability and crash scenario in the main DRF API permission layer (`ApiPermission`).

*   **Architecture Flaw:** The system supports multiple authentication token types (`UserApiToken`, `TeamAPIToken`, `Device`, `OAuthAccessToken`), but they do not share a unified interface for checking event access.
*   **Resulting Bug:** The main `_has_permission` method blindly assumed all `request.auth` objects had an `.events.all()` attribute. This caused a 500 Server Error (`AttributeError`) when using valid `TeamAPIToken` or `Device` authentication to access event-scoped API endpoints.
*   **Remediation:** Refactored the permission check to explicitly use `hasattr` to discover which interface the token supports (`has_event_permission`, `events`, or `get_events_with_any_permission`), falling back safely (failing closed) if none match.

*Note to future investigators:* When working with authentication objects in DRF views within Eventyay, NEVER assume a specific interface (like `.user` or `.events`) exists on `request.auth`. Always check `hasattr` or use `isinstance`.
