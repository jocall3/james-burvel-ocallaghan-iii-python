# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    callback_url: Annotated[object, PropertyInfo(alias="callbackUrl")]
    """Updated URL where webhook events will be sent."""

    events: Iterable[object]
    """Updated list of event types subscribed to."""

    status: Literal["active", "paused", "suspended"]
    """Updated status of the webhook subscription."""
