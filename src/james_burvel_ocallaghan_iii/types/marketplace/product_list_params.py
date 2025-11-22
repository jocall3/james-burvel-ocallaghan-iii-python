# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    category: str
    """Filter products by category."""

    limit: int
    """Maximum number of items to return."""

    offset: int
    """Number of items to skip before starting to collect the result set."""
