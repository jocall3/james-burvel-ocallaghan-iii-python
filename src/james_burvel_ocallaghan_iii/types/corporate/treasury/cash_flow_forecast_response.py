# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = [
    "CashFlowForecastResponse",
    "InflowForecast",
    "InflowForecastBySource",
    "OutflowForecast",
    "OutflowForecastByCategory",
    "ProjectedBalance",
]


class InflowForecastBySource(BaseModel):
    amount: Optional[float] = None

    source: Optional[str] = None


class InflowForecast(BaseModel):
    by_source: Optional[List[InflowForecastBySource]] = FieldInfo(alias="bySource", default=None)

    total_projected: Optional[float] = FieldInfo(alias="totalProjected", default=None)


class OutflowForecastByCategory(BaseModel):
    amount: Optional[float] = None

    category: Optional[str] = None


class OutflowForecast(BaseModel):
    by_category: Optional[List[OutflowForecastByCategory]] = FieldInfo(alias="byCategory", default=None)

    total_projected: Optional[float] = FieldInfo(alias="totalProjected", default=None)


class ProjectedBalance(BaseModel):
    date: Optional[datetime.date] = None

    projected_cash: Optional[float] = FieldInfo(alias="projectedCash", default=None)

    scenario: Optional[Literal["most_likely", "best_case", "worst_case"]] = None


class CashFlowForecastResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-driven actionable recommendations for treasury optimization."""

    currency: str
    """The primary currency of the forecast."""

    forecast_id: str = FieldInfo(alias="forecastId")
    """Unique identifier for the cash flow forecast."""

    inflow_forecast: InflowForecast = FieldInfo(alias="inflowForecast")
    """Forecasted cash inflows categorized by source."""

    liquidity_risk_score: int = FieldInfo(alias="liquidityRiskScore")
    """AI-calculated score (0-100) indicating the risk of liquidity shortfalls."""

    outflow_forecast: OutflowForecast = FieldInfo(alias="outflowForecast")
    """Forecasted cash outflows categorized by spending category."""

    overall_status: Literal["positive_outlook", "neutral", "negative_outlook", "critical_risk"] = FieldInfo(
        alias="overallStatus"
    )
    """Overall assessment of the corporate cash flow outlook."""

    period: str
    """The forecast period (e.g., 'Next 30 Days', 'Q3 2024')."""

    projected_balances: List[ProjectedBalance] = FieldInfo(alias="projectedBalances")
    """Projected cash balances at key dates, potentially across different scenarios."""
