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
    """Average cost per unit of the asset."""

    current_price: float = FieldInfo(alias="currentPrice")
    """Current market price per unit."""

    market_value: float = FieldInfo(alias="marketValue")
    """Current total market value of this holding."""

    name: str
    """Full name of the asset."""

    quantity: float
    """Number of units held."""

    symbol: str
    """Ticker symbol or identifier of the asset."""

    esg_score: Optional[float] = FieldInfo(alias="esgScore", default=None)
    """ESG (Environmental, Social, Governance) score of the holding, if available."""

    gain_loss: Optional[float] = FieldInfo(alias="gainLoss", default=None)
    """Unrealized gain or loss for this specific holding."""

    percentage_of_portfolio: Optional[float] = FieldInfo(alias="percentageOfPortfolio", default=None)
    """Percentage of the total portfolio value represented by this holding."""


class InvestmentPortfolio(BaseModel):
    id: str
    """Unique identifier for the investment portfolio."""

    currency: str
    """The base currency of the portfolio."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the portfolio data was last synced/updated."""

    name: str
    """Name of the portfolio."""

    risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"] = FieldInfo(
        alias="riskTolerance"
    )
    """User-defined or AI-assessed risk tolerance for this portfolio."""

    total_value: float = FieldInfo(alias="totalValue")
    """Current total market value of the portfolio."""

    type: Literal["equities", "bonds", "diversified", "retirement", "crypto", "custom"]
    """Type or strategy of the investment portfolio."""

    ai_performance_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiPerformanceInsights", default=None)
    """AI-generated insights and recommendations related to portfolio performance."""

    ai_rebalancing_frequency: Optional[Literal["never", "monthly", "quarterly", "annually"]] = FieldInfo(
        alias="aiRebalancingFrequency", default=None
    )
    """Frequency at which the AI is configured to suggest or perform rebalancing."""

    holdings: Optional[List[Holding]] = None
    """Detailed list of assets held within the portfolio."""

    today_gain_loss: Optional[float] = FieldInfo(alias="todayGainLoss", default=None)
    """Gain or loss for the current trading day."""

    unrealized_gain_loss: Optional[float] = FieldInfo(alias="unrealizedGainLoss", default=None)
    """Total unrealized gain or loss for the portfolio."""
