# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssetSearchResponse", "AssetSearchResponseItem"]


class AssetSearchResponseItem(BaseModel):
    asset_name: str = FieldInfo(alias="assetName")
    """Full name of the investment asset."""

    asset_symbol: str = FieldInfo(alias="assetSymbol")
    """Ticker symbol of the investment asset."""

    asset_type: Literal["stock", "etf", "mutual_fund", "bond", "crypto"] = FieldInfo(alias="assetType")
    """Type of investment asset."""

    currency: str
    """Currency of the asset."""

    current_price: float = FieldInfo(alias="currentPrice")
    """Current market price of the asset."""

    overall_esg_score: float = FieldInfo(alias="overallESGScore")
    """Overall ESG score (0-10) for the asset."""

    ai_esg_insight: Optional[str] = FieldInfo(alias="aiESGInsight", default=None)
    """AI-generated insight into the asset's ESG profile."""

    environmental_score: Optional[float] = FieldInfo(alias="environmentalScore", default=None)
    """Environmental component of the ESG score."""

    esg_controversies: Optional[List[str]] = FieldInfo(alias="esgControversies", default=None)
    """List of significant ESG controversies associated with the asset."""

    esg_rating_provider: Optional[str] = FieldInfo(alias="esgRatingProvider", default=None)
    """The provider of the ESG rating data."""

    governance_score: Optional[float] = FieldInfo(alias="governanceScore", default=None)
    """Governance component of the ESG score."""

    social_score: Optional[float] = FieldInfo(alias="socialScore", default=None)
    """Social component of the ESG score."""


AssetSearchResponse: TypeAlias = List[AssetSearchResponseItem]
