# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    callback_url: Required[Annotated[str, PropertyInfo(alias="callbackUrl")]]
    """The URL where webhook events will be sent."""

    events: Required[SequenceNotStr[str]]
    """
    A list of event types to subscribe to (e.g., 'transaction.created',
    'account.updated').
    """

    secret: Optional[str]
    """
    Optional: A secret string to use for signing webhook payloads, ensuring
    authenticity. If not provided, one will be generated.
    """
