# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookSubscription"]


class WebhookSubscription(BaseModel):
    id: str
    """Unique identifier for the webhook subscription."""

    callback_url: str = FieldInfo(alias="callbackUrl")
    """The URL to which webhook events will be sent."""

    events: List[str]
    """
    List of event types subscribed to (e.g., 'transaction.created',
    'user.login_failed').
    """

    failure_count: int = FieldInfo(alias="failureCount")
    """Number of consecutive failed delivery attempts."""

    status: Literal["active", "paused", "failed"]
    """Current status of the subscription."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the webhook subscription was created."""

    last_triggered: Optional[datetime] = FieldInfo(alias="lastTriggered", default=None)
    """Timestamp of the last successful webhook delivery."""

    secret: Optional[str] = None
    """
    The shared secret used to sign webhook payloads, null after creation for
    security.
    """
