# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["InvestmentAnalyzeImpactResponse", "BreakdownByEsgFactors", "LowestEsgHolding", "TopEsgHolding"]


class BreakdownByEsgFactors(BaseModel):
    environmental_score: Optional[float] = FieldInfo(alias="environmentalScore", default=None)
    """Environmental component score."""

    governance_score: Optional[float] = FieldInfo(alias="governanceScore", default=None)
    """Governance component score."""

    social_score: Optional[float] = FieldInfo(alias="socialScore", default=None)
    """Social component score."""


class LowestEsgHolding(BaseModel):
    asset_name: Optional[str] = FieldInfo(alias="assetName", default=None)
    """Name of the asset."""

    asset_symbol: Optional[str] = FieldInfo(alias="assetSymbol", default=None)
    """Ticker symbol of the asset."""

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)
    """ESG score of the asset."""


class TopEsgHolding(BaseModel):
    asset_name: Optional[str] = FieldInfo(alias="assetName", default=None)
    """Name of the asset."""

    asset_symbol: Optional[str] = FieldInfo(alias="assetSymbol", default=None)
    """Ticker symbol of the asset."""

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)
    """ESG score of the asset."""


class InvestmentAnalyzeImpactResponse(BaseModel):
    benchmark_esg_score: Optional[float] = FieldInfo(alias="benchmarkESGScore", default=None)
    """Average ESG score of a relevant benchmark (e.g., S&P 500)."""

    breakdown_by_esg_factors: BreakdownByEsgFactors = FieldInfo(alias="breakdownByESGFactors")
    """
    Breakdown of the ESG score into Environmental, Social, and Governance
    components.
    """

    overall_esg_score: float = FieldInfo(alias="overallESGScore")
    """Overall ESG score of the portfolio (0-10)."""

    portfolio_id: str = FieldInfo(alias="portfolioId")
    """The ID of the investment portfolio analyzed."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """AI-generated recommendations to improve the portfolio's ESG impact."""

    ai_summary: Optional[str] = FieldInfo(alias="aiSummary", default=None)
    """AI-generated summary of the ESG analysis."""

    lowest_esg_holdings: Optional[List[LowestEsgHolding]] = FieldInfo(alias="lowestESGHoldings", default=None)
    """List of lowest performing holdings in terms of ESG score."""

    top_esg_holdings: Optional[List[TopEsgHolding]] = FieldInfo(alias="topESGHoldings", default=None)
    """List of top performing holdings in terms of ESG score."""
