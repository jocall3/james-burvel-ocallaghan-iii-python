# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .address_param import AddressParam

__all__ = ["UserRegisterParams"]


class UserRegisterParams(TypedDict, total=False):
    email: Required[str]
    """Unique email address for the user."""

    name: Required[str]
    """Full name of the user."""

    password: Required[str]
    """Secure password for the user account."""

    phone: Required[str]
    """Phone number for SMS verification and communication."""

    address: AddressParam
    """User's residential address (optional for initial registration)."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]
    """User's date of birth (optional for initial registration)."""
