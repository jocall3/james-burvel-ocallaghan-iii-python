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

    scenario: Optional[Literal["most_likely", "worst_case", "best_case"]] = None


class CashFlowForecastResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-generated actionable recommendations for treasury optimization."""

    currency: str
    """The primary currency of the forecast (ISO 4217 code)."""

    forecast_id: str = FieldInfo(alias="forecastId")
    """Unique identifier for the cash flow forecast."""

    inflow_forecast: InflowForecast = FieldInfo(alias="inflowForecast")
    """Detailed forecast of expected cash inflows."""

    liquidity_risk_score: int = FieldInfo(alias="liquidityRiskScore")
    """AI-assessed risk score (0-100) for liquidity issues during the forecast period."""

    outflow_forecast: OutflowForecast = FieldInfo(alias="outflowForecast")
    """Detailed forecast of expected cash outflows."""

    overall_status: Literal["positive_outlook", "stable", "potential_deficit", "critical_deficit"] = FieldInfo(
        alias="overallStatus"
    )
    """Overall assessment of the forecasted cash flow."""

    period: str
    """The time period covered by the forecast."""

    projected_balances: List[ProjectedBalance] = FieldInfo(alias="projectedBalances")
    """
    Projected cash balances at various points in the forecast horizon, possibly
    across scenarios.
    """

    generated_on: Optional[datetime.datetime] = FieldInfo(alias="generatedOn", default=None)
    """Timestamp when the forecast was generated."""
