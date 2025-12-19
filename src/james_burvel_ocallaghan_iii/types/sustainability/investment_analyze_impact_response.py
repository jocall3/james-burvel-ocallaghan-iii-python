# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["InvestmentAnalyzeImpactResponse", "BreakdownByEsgFactors", "LowestEsgHolding", "TopEsgHolding"]


class BreakdownByEsgFactors(BaseModel):
    """Breakdown of the portfolio's ESG score by individual factors."""

    environmental_score: Optional[object] = FieldInfo(alias="environmentalScore", default=None)

    governance_score: Optional[object] = FieldInfo(alias="governanceScore", default=None)

    social_score: Optional[object] = FieldInfo(alias="socialScore", default=None)


class LowestEsgHolding(BaseModel):
    asset_name: Optional[object] = FieldInfo(alias="assetName", default=None)

    asset_symbol: Optional[object] = FieldInfo(alias="assetSymbol", default=None)

    esg_score: Optional[object] = FieldInfo(alias="esgScore", default=None)


class TopEsgHolding(BaseModel):
    asset_name: Optional[object] = FieldInfo(alias="assetName", default=None)

    asset_symbol: Optional[object] = FieldInfo(alias="assetSymbol", default=None)

    esg_score: Optional[object] = FieldInfo(alias="esgScore", default=None)


class InvestmentAnalyzeImpactResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-driven recommendations to improve the portfolio's ESG impact."""

    benchmark_esg_score: object = FieldInfo(alias="benchmarkESGScore")
    """Average ESG score of a relevant market benchmark for comparison."""

    breakdown_by_esg_factors: BreakdownByEsgFactors = FieldInfo(alias="breakdownByESGFactors")
    """Breakdown of the portfolio's ESG score by individual factors."""

    lowest_esg_holdings: List[LowestEsgHolding] = FieldInfo(alias="lowestESGHoldings")
    """Lowest holdings in the portfolio by ESG score."""

    overall_esg_score: object = FieldInfo(alias="overallESGScore")
    """Overall ESG score of the entire portfolio (0-10)."""

    portfolio_id: object = FieldInfo(alias="portfolioId")
    """ID of the investment portfolio analyzed."""

    top_esg_holdings: List[TopEsgHolding] = FieldInfo(alias="topESGHoldings")
    """Top holdings in the portfolio by ESG score."""
