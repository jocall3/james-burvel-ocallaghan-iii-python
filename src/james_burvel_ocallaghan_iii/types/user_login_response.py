# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserLoginResponse"]


class UserLoginResponse(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)
    """JWT access token for authenticated API requests."""

    expires_in: Optional[int] = FieldInfo(alias="expiresIn", default=None)
    """Lifetime of the access token in seconds."""

    refresh_token: Optional[str] = FieldInfo(alias="refreshToken", default=None)
    """Token used to obtain a new access token without re-authenticating."""

    token_type: Optional[str] = FieldInfo(alias="tokenType", default=None)
    """Type of the token, usually 'Bearer'."""
