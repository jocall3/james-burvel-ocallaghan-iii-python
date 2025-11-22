# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..address_param import AddressParam

__all__ = ["MeUpdateParams"]


class MeUpdateParams(TypedDict, total=False):
    address: AddressParam
    """Updated residential address of the user."""

    ai_persona: Annotated[str, PropertyInfo(alias="aiPersona")]
    """User's self-selected or AI-adjusted financial persona."""

    name: str
    """Updated full name of the user."""

    phone: str
    """Updated phone number of the user."""
