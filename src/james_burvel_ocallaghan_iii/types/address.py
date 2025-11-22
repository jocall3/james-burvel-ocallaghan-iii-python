# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    city: Optional[str] = None
    """City."""

    country: Optional[str] = None
    """Country."""

    state: Optional[str] = None
    """State or province (if applicable)."""

    street: Optional[str] = None
    """Street name and number."""

    zip: Optional[str] = None
    """Postal or ZIP code."""
