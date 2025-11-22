# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    callback_url: Required[Annotated[str, PropertyInfo(alias="callbackUrl")]]
    """The URL to which webhook events will be sent."""

    events: Required[SequenceNotStr[str]]
    """List of event types to subscribe to."""

    secret: Optional[str]
    """Optional: A custom shared secret for verifying webhook payloads.

    If omitted, one will be generated.
    """
