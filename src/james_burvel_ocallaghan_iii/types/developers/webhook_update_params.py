# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The updated URL for webhook deliveries."""

    events: SequenceNotStr[str]
    """The new list of event types to subscribe to. Overwrites existing list."""

    secret: Optional[str]
    """Optional: A new secret string to update or set for webhook payload signing."""

    status: Literal["active", "paused"]
    """Updated status of the subscription."""
