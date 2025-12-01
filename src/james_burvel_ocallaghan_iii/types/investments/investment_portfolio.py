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
    """Total market value of the holding."""

    name: str
    """Full name of the investment asset."""

    percentage_of_portfolio: float = FieldInfo(alias="percentageOfPortfolio")
    """Percentage of the total portfolio value this holding represents."""

    quantity: float
    """Number of units held."""

    symbol: str
    """Stock ticker or asset symbol."""

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)
    """Overall ESG (Environmental, Social, Governance) score of the asset (0-10)."""


class InvestmentPortfolio(BaseModel):
    id: str
    """Unique identifier for the investment portfolio."""

    currency: str
    """ISO 4217 currency code of the portfolio."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the portfolio data was last updated."""

    name: str
    """Name of the portfolio."""

    risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"] = FieldInfo(
        alias="riskTolerance"
    )
    """User's stated or AI-assessed risk tolerance for this portfolio."""

    today_gain_loss: float = FieldInfo(alias="todayGainLoss")
    """Daily gain or loss on the portfolio."""

    total_value: float = FieldInfo(alias="totalValue")
    """Current total market value of the portfolio."""

    type: Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"]
    """General type or strategy of the portfolio."""

    unrealized_gain_loss: float = FieldInfo(alias="unrealizedGainLoss")
    """Total unrealized gain or loss on the portfolio."""

    ai_performance_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiPerformanceInsights", default=None)
    """AI-driven insights into portfolio performance and market outlook."""

    ai_rebalancing_frequency: Optional[Literal["monthly", "quarterly", "semi_annually", "annually", "never"]] = (
        FieldInfo(alias="aiRebalancingFrequency", default=None)
    )
    """Frequency at which AI-driven rebalancing is set to occur."""

    holdings: Optional[List[Holding]] = None
    """List of individual assets held in the portfolio."""
