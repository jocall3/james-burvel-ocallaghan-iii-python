# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .address_param import AddressParam

__all__ = ["UserRegisterParams"]


class UserRegisterParams(TypedDict, total=False):
    email: Required[str]
    """Email address for registration and login."""

    name: Required[str]
    """Full name of the user."""

    password: Required[str]
    """User's chosen password."""

    address: AddressParam
    """Optional initial address details."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]
    """Optional date of birth (YYYY-MM-DD)."""

    phone: Optional[str]
    """Optional phone number for MFA or recovery."""
