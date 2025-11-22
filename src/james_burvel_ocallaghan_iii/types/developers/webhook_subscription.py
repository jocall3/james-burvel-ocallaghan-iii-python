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
    """The URL to which webhook events are sent."""

    events: List[str]
    """
    List of event types subscribed to (e.g., 'transaction.created',
    'account.updated').
    """

    failure_count: int = FieldInfo(alias="failureCount")
    """Consecutive failure count for webhook deliveries (resets on success)."""

    status: Literal["active", "paused", "suspended"]
    """Current status of the subscription."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the subscription was created."""

    last_triggered: Optional[datetime] = FieldInfo(alias="lastTriggered", default=None)
    """Timestamp of the last successful webhook delivery."""
