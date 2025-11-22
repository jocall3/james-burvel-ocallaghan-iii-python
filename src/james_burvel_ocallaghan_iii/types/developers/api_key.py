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
    """The visible prefix of the API key (the full key is secret and not exposed)."""

    scopes: List[str]
    """List of OAuth2 scopes associated with this API key."""

    status: Literal["active", "revoked", "expired"]
    """Current status of the API key."""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Timestamp when the API key will expire, if set."""

    last_used: Optional[datetime] = FieldInfo(alias="lastUsed", default=None)
    """Timestamp of the last successful use of this API key."""

    name: Optional[str] = None
    """A friendly name given to the API key for identification."""
