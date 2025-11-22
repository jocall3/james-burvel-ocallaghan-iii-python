# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PasswordResetConfirmParams"]


class PasswordResetConfirmParams(TypedDict, total=False):
    identifier: Required[str]
    """User's email or phone number used for verification."""

    new_password: Required[Annotated[str, PropertyInfo(alias="newPassword")]]
    """The new password for the user account."""

    verification_code: Required[Annotated[str, PropertyInfo(alias="verificationCode")]]
    """The verification code received via email or SMS."""
