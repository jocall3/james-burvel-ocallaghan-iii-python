# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserLoginResponse"]


class UserLoginResponse(BaseModel):
    access_token: object = FieldInfo(alias="accessToken")
    """JWT access token to authenticate subsequent API requests."""

    expires_in: object = FieldInfo(alias="expiresIn")
    """Lifetime of the access token in seconds."""

    refresh_token: object = FieldInfo(alias="refreshToken")
    """Token used to obtain new access tokens without re-authenticating."""

    token_type: object = FieldInfo(alias="tokenType")
    """Type of the access token."""
