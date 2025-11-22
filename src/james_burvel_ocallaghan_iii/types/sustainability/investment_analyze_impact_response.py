# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["InvestmentAnalyzeImpactResponse", "BreakdownByEsgFactors", "LowestEsgHolding", "TopEsgHolding"]


class BreakdownByEsgFactors(BaseModel):
    environmental_score: Optional[float] = FieldInfo(alias="environmentalScore", default=None)

    governance_score: Optional[float] = FieldInfo(alias="governanceScore", default=None)

    social_score: Optional[float] = FieldInfo(alias="socialScore", default=None)


class LowestEsgHolding(BaseModel):
    asset_name: Optional[str] = FieldInfo(alias="assetName", default=None)

    asset_symbol: Optional[str] = FieldInfo(alias="assetSymbol", default=None)

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)


class TopEsgHolding(BaseModel):
    asset_name: Optional[str] = FieldInfo(alias="assetName", default=None)

    asset_symbol: Optional[str] = FieldInfo(alias="assetSymbol", default=None)

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)


class InvestmentAnalyzeImpactResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-driven recommendations to improve the ESG profile of the portfolio."""

    benchmark_esg_score: float = FieldInfo(alias="benchmarkESGScore")
    """Average ESG score for a comparable market benchmark."""

    breakdown_by_esg_factors: BreakdownByEsgFactors = FieldInfo(alias="breakdownByESGFactors")
    """
    Breakdown of the portfolio's ESG score into environmental, social, and
    governance components.
    """

    lowest_esg_holdings: List[LowestEsgHolding] = FieldInfo(alias="lowestESGHoldings")
    """List of lowest-scoring holdings by their individual ESG score."""

    overall_esg_score: float = FieldInfo(alias="overallESGScore")
    """Overall aggregated ESG score for the entire portfolio."""

    portfolio_id: str = FieldInfo(alias="portfolioId")
    """The ID of the investment portfolio analyzed."""

    top_esg_holdings: List[TopEsgHolding] = FieldInfo(alias="topESGHoldings")
    """List of top holdings by their individual ESG score."""
