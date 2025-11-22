# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str
    """Unique identifier for the API key."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the API key was created."""

    prefix: str
    """A short, non-sensitive prefix of the API key for identification."""

    scopes: List[str]
    """A list of OAuth2 scopes granted to this API key."""

    status: Literal["active", "revoked", "expired"]
    """Current status of the API key."""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Optional: Timestamp when the API key will expire."""

    last_used: Optional[datetime] = FieldInfo(alias="lastUsed", default=None)
    """Timestamp of the last successful API call made with this key."""

    name: Optional[str] = None
    """A user-defined name or description for the API key."""
