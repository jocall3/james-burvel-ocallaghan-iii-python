# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["InvestmentPortfolio", "Holding"]


class Holding(BaseModel):
    average_cost: float = FieldInfo(alias="averageCost")
    """Average cost per unit."""

    current_price: float = FieldInfo(alias="currentPrice")
    """Current market price per unit."""

    market_value: float = FieldInfo(alias="marketValue")
    """Total market value of this holding."""

    name: str
    """Full name of the asset."""

    percentage_of_portfolio: float = FieldInfo(alias="percentageOfPortfolio")
    """Percentage this holding represents of the total portfolio value."""

    quantity: float
    """Number of units held."""

    symbol: str
    """Ticker symbol of the asset."""

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)
    """ESG (Environmental, Social, Governance) score for the asset."""

    gain_loss: Optional[float] = FieldInfo(alias="gainLoss", default=None)
    """Total gain or loss for this holding."""


class InvestmentPortfolio(BaseModel):
    id: str
    """Unique identifier for the investment portfolio."""

    currency: str
    """Base currency of the portfolio."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the portfolio data was last synced/updated."""

    name: str
    """User-friendly name of the portfolio."""

    risk_tolerance: Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"] = FieldInfo(
        alias="riskTolerance"
    )
    """User's stated or AI-derived risk tolerance for this portfolio."""

    total_value: float = FieldInfo(alias="totalValue")
    """Current total market value of the portfolio."""

    type: Literal["equities", "bonds", "diversified", "crypto", "reit", "commodities", "other"]
    """Primary asset type or strategy of the portfolio."""

    ai_performance_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiPerformanceInsights", default=None)
    """AI-driven insights into portfolio performance and market outlook."""

    ai_rebalancing_frequency: Optional[Literal["monthly", "quarterly", "semi_annually", "annually", "manual"]] = (
        FieldInfo(alias="aiRebalancingFrequency", default=None)
    )
    """
    Frequency at which the AI is configured to suggest or perform rebalancing for
    this portfolio.
    """

    holdings: Optional[List[Holding]] = None
    """Detailed breakdown of assets held within the portfolio."""

    today_gain_loss: Optional[float] = FieldInfo(alias="todayGainLoss", default=None)
    """Today's gain or loss for the portfolio."""

    unrealized_gain_loss: Optional[float] = FieldInfo(alias="unrealizedGainLoss", default=None)
    """Total unrealized gain or loss for the portfolio."""
