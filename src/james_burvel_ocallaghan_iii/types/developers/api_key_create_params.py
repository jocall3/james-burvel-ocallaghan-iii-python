# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """A friendly name for the new API key."""

    scopes: Required[SequenceNotStr[str]]
    """List of OAuth2 scopes that this API key should have access to."""

    expires_in_days: Annotated[Optional[int], PropertyInfo(alias="expiresInDays")]
    """Optional: Number of days until the API key expires.

    If null, it does not expire.
    """
