# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """A descriptive name for the new API key."""

    scopes: Required[SequenceNotStr[str]]
    """List of desired permissions (scopes) for the API key."""

    expires_in_days: Annotated[Optional[int], PropertyInfo(alias="expiresInDays")]
    """Optional: Number of days until the API key expires.

    If not provided, it will not expire.
    """

    is_secret_key: Annotated[bool, PropertyInfo(alias="isSecretKey")]
    """
    If true, generates a secret key (suitable for server-to-server) with a 'db*sk*'
    prefix. Otherwise, generates a public key ('db*pk*').
    """
