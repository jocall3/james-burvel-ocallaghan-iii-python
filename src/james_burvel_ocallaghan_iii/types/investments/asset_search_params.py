# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssetSearchParams"]


class AssetSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query for asset name or symbol."""

    limit: int
    """Maximum number of items to return in a single page."""

    min_esg_score: Annotated[float, PropertyInfo(alias="minESGScore")]
    """Minimum desired ESG score (0-10)."""

    offset: int
    """Number of items to skip before starting to collect the result set."""
