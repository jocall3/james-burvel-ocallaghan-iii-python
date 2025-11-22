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
    """The URL where webhook events will be sent."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the subscription was created."""

    events: List[str]
    """List of event types subscribed to."""

    status: Literal["active", "paused", "suspended"]
    """Current status of the webhook subscription."""

    failure_count: Optional[int] = FieldInfo(alias="failureCount", default=None)
    """Number of consecutive failed delivery attempts."""

    last_triggered: Optional[datetime] = FieldInfo(alias="lastTriggered", default=None)
    """Timestamp of the last successful webhook delivery."""

    secret: Optional[str] = None
    """The shared secret used to sign webhook payloads, for verification.

    Only returned on creation.
    """
