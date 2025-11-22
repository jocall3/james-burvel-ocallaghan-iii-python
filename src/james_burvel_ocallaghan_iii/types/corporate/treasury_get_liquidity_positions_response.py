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
    """Amount in this account type."""

    type: Optional[str] = None
    """Account type."""


class AILiquidityAssessment(BaseModel):
    message: str
    """Detailed message from AI."""

    status: Literal["optimal", "sufficient", "constrained", "critical"]
    """AI's overall assessment of liquidity."""


class CurrencyBreakdown(BaseModel):
    amount: Optional[float] = None
    """Amount in this currency."""

    currency: Optional[str] = None
    """Currency code."""

    percentage: Optional[float] = None
    """Percentage of total liquid assets."""


class ShortTermInvestments(BaseModel):
    maturing_next30_days: Optional[float] = FieldInfo(alias="maturingNext30Days", default=None)
    """Amount of investments maturing in the next 30 days."""

    total_value: Optional[float] = FieldInfo(alias="totalValue", default=None)
    """Total value of short-term investments."""

    yield_percentage: Optional[float] = FieldInfo(alias="yieldPercentage", default=None)
    """Average yield percentage of short-term investments."""


class TreasuryGetLiquidityPositionsResponse(BaseModel):
    account_type_breakdown: List[AccountTypeBreakdown] = FieldInfo(alias="accountTypeBreakdown")
    """
    Breakdown of liquid assets by account type (e.g., Checking, Savings, Money
    Market).
    """

    ai_liquidity_assessment: AILiquidityAssessment = FieldInfo(alias="aiLiquidityAssessment")

    currency_breakdown: List[CurrencyBreakdown] = FieldInfo(alias="currencyBreakdown")
    """Breakdown of liquid assets by currency."""

    short_term_investments: ShortTermInvestments = FieldInfo(alias="shortTermInvestments")
    """Details on short-term, highly liquid investments."""

    snapshot_time: datetime = FieldInfo(alias="snapshotTime")
    """Timestamp of the liquidity snapshot."""

    total_liquid_assets: float = FieldInfo(alias="totalLiquidAssets")
    """Total value of all liquid assets across accounts and short-term investments."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """AI-generated recommendations for optimizing liquidity."""
