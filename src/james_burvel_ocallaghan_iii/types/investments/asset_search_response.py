# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssetSearchResponse", "Data"]


class Data(BaseModel):
    asset_name: object = FieldInfo(alias="assetName")
    """Full name of the investment asset."""

    asset_symbol: object = FieldInfo(alias="assetSymbol")
    """Symbol of the investment asset."""

    asset_type: Literal["stock", "etf", "mutual_fund", "bond"] = FieldInfo(alias="assetType")
    """Type of the investment asset."""

    currency: object
    """Currency of the asset's price."""

    current_price: object = FieldInfo(alias="currentPrice")
    """Current market price of the asset."""

    overall_esg_score: object = FieldInfo(alias="overallESGScore")
    """Overall ESG score (0-10), higher is better."""

    ai_esg_insight: Optional[object] = FieldInfo(alias="aiESGInsight", default=None)
    """AI-generated insight summarizing the ESG profile."""

    environmental_score: Optional[object] = FieldInfo(alias="environmentalScore", default=None)
    """Environmental component of the ESG score."""

    esg_controversies: Optional[List[object]] = FieldInfo(alias="esgControversies", default=None)
    """List of any significant ESG-related controversies associated with the asset."""

    esg_rating_provider: Optional[object] = FieldInfo(alias="esgRatingProvider", default=None)
    """Provider of the ESG rating (e.g., MSCI, Sustainalytics)."""

    governance_score: Optional[object] = FieldInfo(alias="governanceScore", default=None)
    """Governance component of the ESG score."""

    social_score: Optional[object] = FieldInfo(alias="socialScore", default=None)
    """Social component of the ESG score."""


class AssetSearchResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
