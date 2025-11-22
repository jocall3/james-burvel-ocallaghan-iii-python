# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssetSearchResponse", "AssetSearchResponseItem"]


class AssetSearchResponseItem(BaseModel):
    asset_name: str = FieldInfo(alias="assetName")
    """Full name of the asset."""

    asset_symbol: str = FieldInfo(alias="assetSymbol")
    """Ticker symbol or identifier of the asset."""

    asset_type: Literal["stock", "etf", "mutual_fund", "bond"] = FieldInfo(alias="assetType")
    """Type of investment asset."""

    currency: str
    """Currency of the asset."""

    current_price: float = FieldInfo(alias="currentPrice")
    """Current market price of the asset."""

    overall_esg_score: float = FieldInfo(alias="overallESGScore")
    """Overall ESG score (typically 0-10, higher is better)."""

    ai_esg_insight: Optional[str] = FieldInfo(alias="aiESGInsight", default=None)
    """AI-generated commentary on the asset's ESG profile."""

    environmental_score: Optional[float] = FieldInfo(alias="environmentalScore", default=None)
    """Specific environmental component score."""

    esg_controversies: Optional[List[str]] = FieldInfo(alias="esgControversies", default=None)
    """List of notable ESG controversies associated with the asset."""

    esg_rating_provider: Optional[str] = FieldInfo(alias="esgRatingProvider", default=None)
    """The provider of the ESG rating (e.g., MSCI, Sustainalytics)."""

    governance_score: Optional[float] = FieldInfo(alias="governanceScore", default=None)
    """Specific governance component score."""

    social_score: Optional[float] = FieldInfo(alias="socialScore", default=None)
    """Specific social component score."""


AssetSearchResponse: TypeAlias = List[AssetSearchResponseItem]
