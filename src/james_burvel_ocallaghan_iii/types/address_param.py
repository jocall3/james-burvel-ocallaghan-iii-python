# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AddressParam"]


class AddressParam(TypedDict, total=False):
    city: str

    country: str

    state: str

    street: str

    zip: str
