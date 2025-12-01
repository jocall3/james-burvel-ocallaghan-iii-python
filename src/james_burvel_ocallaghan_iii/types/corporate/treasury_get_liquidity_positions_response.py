# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = [
    "TreasuryGetLiquidityPositionsResponse",
    "AccountTypeBreakdown",
    "AILiquidityAssessment",
    "CurrencyBreakdown",
    "ShortTermInvestments",
]


class AccountTypeBreakdown(BaseModel):
    amount: Optional[object] = None

    type: Optional[object] = None


class AILiquidityAssessment(BaseModel):
    message: Optional[object] = None

    status: Optional[Literal["optimal", "sufficient", "tight", "critical"]] = None


class CurrencyBreakdown(BaseModel):
    amount: Optional[object] = None

    currency: Optional[object] = None

    percentage: Optional[object] = None


class ShortTermInvestments(BaseModel):
    maturing_next30_days: Optional[object] = FieldInfo(alias="maturingNext30Days", default=None)

    total_value: Optional[object] = FieldInfo(alias="totalValue", default=None)


class TreasuryGetLiquidityPositionsResponse(BaseModel):
    account_type_breakdown: List[AccountTypeBreakdown] = FieldInfo(alias="accountTypeBreakdown")
    """Breakdown of liquid assets by account type."""

    ai_liquidity_assessment: AILiquidityAssessment = FieldInfo(alias="aiLiquidityAssessment")
    """AI's overall assessment of liquidity."""

    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-generated recommendations for liquidity management."""

    currency_breakdown: List[CurrencyBreakdown] = FieldInfo(alias="currencyBreakdown")
    """Breakdown of liquid assets by currency."""

    short_term_investments: ShortTermInvestments = FieldInfo(alias="shortTermInvestments")
    """Details on short-term investments contributing to liquidity."""

    snapshot_time: object = FieldInfo(alias="snapshotTime")
    """Timestamp of the liquidity snapshot."""

    total_liquid_assets: object = FieldInfo(alias="totalLiquidAssets")
    """Total value of all liquid assets across the organization."""
