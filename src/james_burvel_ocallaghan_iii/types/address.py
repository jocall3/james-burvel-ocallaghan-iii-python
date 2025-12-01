# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    city: Optional[object] = None

    country: Optional[object] = None

    state: Optional[object] = None

    street: Optional[object] = None

    zip: Optional[object] = None
