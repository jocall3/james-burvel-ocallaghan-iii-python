# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .address_param import AddressParam

__all__ = ["UserRegisterParams"]


class UserRegisterParams(TypedDict, total=False):
    email: Required[object]
    """Email address for registration and login."""

    name: Required[object]
    """Full name of the user."""

    password: Required[object]
    """User's chosen password."""

    address: AddressParam

    date_of_birth: Annotated[object, PropertyInfo(alias="dateOfBirth")]
    """Optional date of birth (YYYY-MM-DD)."""

    phone: object
    """Optional phone number for MFA or recovery."""
