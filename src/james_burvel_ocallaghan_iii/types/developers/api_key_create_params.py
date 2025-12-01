# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[object]
    """A descriptive name for the API key."""

    scopes: Required[Iterable[object]]
    """List of permissions to grant to this API key."""

    expires_in_days: Annotated[object, PropertyInfo(alias="expiresInDays")]
    """Optional: Number of days until the API key expires.

    If omitted, it will not expire.
    """
