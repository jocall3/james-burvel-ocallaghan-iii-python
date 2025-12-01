# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserLoginParams"]


class UserLoginParams(TypedDict, total=False):
    email: Required[object]
    """User's email address."""

    password: Required[object]
    """User's password."""

    mfa_code: Annotated[object, PropertyInfo(alias="mfaCode")]
    """Optional: Multi-factor authentication code, if required."""
