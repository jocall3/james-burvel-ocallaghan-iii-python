# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserLoginParams"]


class UserLoginParams(TypedDict, total=False):
    email: Required[str]
    """User's email address."""

    password: Required[str]
    """User's password."""

    mfa_code: Annotated[Optional[str], PropertyInfo(alias="mfaCode")]
    """Multi-factor authentication code, if required."""
