# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    callback_url: Required[Annotated[str, PropertyInfo(alias="callbackUrl")]]
    """The URL to which webhook events will be sent."""

    events: Required[SequenceNotStr[str]]
    """
    List of event types to subscribe to (e.g., 'transaction.created',
    'account.updated').
    """

    secret: Optional[str]
    """Optional: A secret string for signing webhook payloads.

    If not provided, one will be auto-generated.
    """

    status: Literal["active", "paused"]
    """Initial status of the subscription."""
