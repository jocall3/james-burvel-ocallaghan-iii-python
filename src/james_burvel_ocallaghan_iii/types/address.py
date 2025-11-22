# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    state: Optional[str] = None

    street: Optional[str] = None

    zip: Optional[str] = None
