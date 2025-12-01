# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardFreezeParams"]


class CardFreezeParams(TypedDict, total=False):
    freeze: Required[object]
    """Set to `true` to freeze the card, `false` to unfreeze."""
