# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """New URL for the webhook endpoint."""

    events: Optional[SequenceNotStr[str]]
    """Updated list of event types to subscribe to."""

    secret: Optional[str]
    """Optional: A new secret string for signing webhook payloads.

    Providing this will replace the existing secret.
    """

    status: Literal["active", "paused"]
    """New status for the subscription."""
