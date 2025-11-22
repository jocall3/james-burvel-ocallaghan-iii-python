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
    """Environmental, Social, and Governance (ESG) score for the asset."""

    gain_loss: Optional[float] = FieldInfo(alias="gainLoss", default=None)
    """Unrealized gain/loss for this specific holding."""


class InvestmentPortfolio(BaseModel):
    id: str
    """Unique identifier for the investment portfolio."""

    currency: str
    """Currency of the portfolio (ISO 4217 code)."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the portfolio data was last updated."""

    name: str
    """User-defined name of the portfolio."""

    risk_tolerance: Literal["low", "medium", "aggressive", "very_aggressive"] = FieldInfo(alias="riskTolerance")
    """User's stated or AI-assessed risk tolerance for this portfolio."""

    today_gain_loss: float = FieldInfo(alias="todayGainLoss")
    """Gain or loss for the current trading day."""

    total_value: float = FieldInfo(alias="totalValue")
    """Current total market value of the portfolio."""

    type: Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"]
    """Type of investment portfolio."""

    unrealized_gain_loss: float = FieldInfo(alias="unrealizedGainLoss")
    """Total unrealized gain or loss on the portfolio."""

    ai_performance_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiPerformanceInsights", default=None)
    """AI-generated insights into portfolio performance and market outlook."""

    ai_rebalancing_frequency: Optional[Literal["never", "monthly", "quarterly", "semi_annually", "annually"]] = (
        FieldInfo(alias="aiRebalancingFrequency", default=None)
    )
    """Frequency at which AI should suggest or perform rebalancing."""

    holdings: Optional[List[Holding]] = None
    """Detailed list of assets currently held in the portfolio."""
