# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AddressParam"]


class AddressParam(TypedDict, total=False):
    city: str
    """City."""

    country: str
    """Country."""

    state: Optional[str]
    """State or province (if applicable)."""

    street: str
    """Street name and number."""

    zip: str
    """Postal or ZIP code."""
