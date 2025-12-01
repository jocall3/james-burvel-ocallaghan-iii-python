# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    callback_url: Required[Annotated[object, PropertyInfo(alias="callbackUrl")]]
    """The URL to which webhook events will be sent."""

    events: Required[Iterable[object]]
    """List of event types to subscribe to."""

    secret: object
    """Optional: A custom shared secret for verifying webhook payloads.

    If omitted, one will be generated.
    """
