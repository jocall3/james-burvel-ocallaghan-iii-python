# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["InvestmentPortfolio", "Holding"]


class Holding(BaseModel):
    average_cost: object = FieldInfo(alias="averageCost")
    """Average cost per unit."""

    current_price: object = FieldInfo(alias="currentPrice")
    """Current market price per unit."""

    market_value: object = FieldInfo(alias="marketValue")
    """Total market value of the holding."""

    name: object
    """Full name of the investment asset."""

    percentage_of_portfolio: object = FieldInfo(alias="percentageOfPortfolio")
    """Percentage of the total portfolio value this holding represents."""

    quantity: object
    """Number of units held."""

    symbol: object
    """Stock ticker or asset symbol."""

    esg_score: Optional[object] = FieldInfo(alias="esgScore", default=None)
    """Overall ESG (Environmental, Social, Governance) score of the asset (0-10)."""


class InvestmentPortfolio(BaseModel):
    id: object
    """Unique identifier for the investment portfolio."""

    currency: object
    """ISO 4217 currency code of the portfolio."""

    last_updated: object = FieldInfo(alias="lastUpdated")
    """Timestamp when the portfolio data was last updated."""

    name: object
    """Name of the portfolio."""

    risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"] = FieldInfo(
        alias="riskTolerance"
    )
    """User's stated or AI-assessed risk tolerance for this portfolio."""

    today_gain_loss: object = FieldInfo(alias="todayGainLoss")
    """Daily gain or loss on the portfolio."""

    total_value: object = FieldInfo(alias="totalValue")
    """Current total market value of the portfolio."""

    type: Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"]
    """General type or strategy of the portfolio."""

    unrealized_gain_loss: object = FieldInfo(alias="unrealizedGainLoss")
    """Total unrealized gain or loss on the portfolio."""

    ai_performance_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiPerformanceInsights", default=None)
    """AI-driven insights into portfolio performance and market outlook."""

    ai_rebalancing_frequency: Optional[Literal["monthly", "quarterly", "semi_annually", "annually", "never"]] = (
        FieldInfo(alias="aiRebalancingFrequency", default=None)
    )
    """Frequency at which AI-driven rebalancing is set to occur."""

    holdings: Optional[List[Holding]] = None
    """List of individual assets held in the portfolio."""
