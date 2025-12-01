# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssetSearchParams"]


class AssetSearchParams(TypedDict, total=False):
    query: Required[object]
    """Search query for asset name or symbol."""

    limit: object
    """Maximum number of items to return in a single page."""

    min_esg_score: Annotated[object, PropertyInfo(alias="minESGScore")]
    """Minimum desired ESG score (0-10)."""

    offset: object
    """Number of items to skip before starting to collect the result set."""
