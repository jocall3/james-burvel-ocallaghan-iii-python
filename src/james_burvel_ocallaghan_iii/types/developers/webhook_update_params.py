# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The new URL where webhook events should be sent."""

    events: SequenceNotStr[str]
    """The updated list of event types to subscribe to.

    Sending an empty array might disable all events.
    """

    status: Literal["active", "paused", "suspended"]
    """The new status for the webhook subscription (e.g., 'active', 'paused')."""
