# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: object
    """Unique identifier for the API key."""

    created_at: object = FieldInfo(alias="createdAt")
    """Timestamp when the API key was created."""

    prefix: object
    """The non-secret prefix of the API key, used for identification."""

    scopes: List[object]
    """List of permissions granted to this API key."""

    status: Literal["active", "revoked", "expired"]
    """Current status of the API key."""

    expires_at: Optional[object] = FieldInfo(alias="expiresAt", default=None)
    """Timestamp when the API key will expire, if set."""

    last_used: Optional[object] = FieldInfo(alias="lastUsed", default=None)
    """Timestamp of the last time this API key was used."""
