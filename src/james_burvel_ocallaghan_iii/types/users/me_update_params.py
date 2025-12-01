# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..address_param import AddressParam
from .me.user_preferences_param import UserPreferencesParam

__all__ = ["MeUpdateParams"]


class MeUpdateParams(TypedDict, total=False):
    address: AddressParam
    """Updated address details."""

    name: str
    """Updated full name of the user."""

    phone: Optional[str]
    """Updated primary phone number of the user."""

    preferences: UserPreferencesParam
    """Updated personalization preferences."""
