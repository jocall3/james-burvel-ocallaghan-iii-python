# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserLoginResponse"]


class UserLoginResponse(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")
    """JWT access token to authenticate subsequent API requests."""

    expires_in: int = FieldInfo(alias="expiresIn")
    """Lifetime of the access token in seconds."""

    refresh_token: str = FieldInfo(alias="refreshToken")
    """Token used to obtain new access tokens without re-authenticating."""

    token_type: str = FieldInfo(alias="tokenType")
    """Type of the access token."""
