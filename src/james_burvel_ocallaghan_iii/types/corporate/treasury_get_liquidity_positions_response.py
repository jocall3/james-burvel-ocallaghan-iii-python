# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
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
    amount: Optional[float] = None

    type: Optional[str] = None


class AILiquidityAssessment(BaseModel):
    message: Optional[str] = None

    status: Optional[Literal["optimal", "sufficient", "constrained", "critical"]] = None


class CurrencyBreakdown(BaseModel):
    amount: Optional[float] = None

    currency: Optional[str] = None

    percentage: Optional[float] = None


class ShortTermInvestments(BaseModel):
    maturing_next30_days: Optional[float] = FieldInfo(alias="maturingNext30Days", default=None)

    total_value: Optional[float] = FieldInfo(alias="totalValue", default=None)


class TreasuryGetLiquidityPositionsResponse(BaseModel):
    account_type_breakdown: List[AccountTypeBreakdown] = FieldInfo(alias="accountTypeBreakdown")
    """
    Breakdown of liquid assets by account type (e.g., Checking, Savings, Money
    Market).
    """

    ai_liquidity_assessment: AILiquidityAssessment = FieldInfo(alias="aiLiquidityAssessment")
    """AI's overall assessment of the current liquidity posture."""

    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-generated actionable recommendations for liquidity management."""

    currency_breakdown: List[CurrencyBreakdown] = FieldInfo(alias="currencyBreakdown")
    """Breakdown of liquid assets by currency."""

    snapshot_time: datetime = FieldInfo(alias="snapshotTime")
    """Timestamp of the liquidity snapshot."""

    total_liquid_assets: float = FieldInfo(alias="totalLiquidAssets")
    """Total value of all liquid assets across the organization."""

    short_term_investments: Optional[ShortTermInvestments] = FieldInfo(alias="shortTermInvestments", default=None)
    """Overview of short-term investment holdings."""
