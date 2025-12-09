# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    amount: Optional[object] = None

    source: Optional[object] = None


class InflowForecast(BaseModel):
    """Forecast of cash inflows by source."""

    by_source: Optional[List[InflowForecastBySource]] = FieldInfo(alias="bySource", default=None)

    total_projected: Optional[object] = FieldInfo(alias="totalProjected", default=None)


class OutflowForecastByCategory(BaseModel):
    amount: Optional[object] = None

    category: Optional[object] = None


class OutflowForecast(BaseModel):
    """Forecast of cash outflows by category."""

    by_category: Optional[List[OutflowForecastByCategory]] = FieldInfo(alias="byCategory", default=None)

    total_projected: Optional[object] = FieldInfo(alias="totalProjected", default=None)


class ProjectedBalance(BaseModel):
    date: Optional[object] = None

    projected_cash: Optional[object] = FieldInfo(alias="projectedCash", default=None)

    scenario: Optional[Literal["most_likely", "best_case", "worst_case"]] = None


class CashFlowForecastResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-generated recommendations for treasury optimization."""

    currency: object
    """The currency of the forecast."""

    forecast_id: object = FieldInfo(alias="forecastId")
    """Unique identifier for the cash flow forecast report."""

    inflow_forecast: InflowForecast = FieldInfo(alias="inflowForecast")
    """Forecast of cash inflows by source."""

    liquidity_risk_score: object = FieldInfo(alias="liquidityRiskScore")
    """AI-assessed risk score for liquidity (0-100, lower is better)."""

    outflow_forecast: OutflowForecast = FieldInfo(alias="outflowForecast")
    """Forecast of cash outflows by category."""

    overall_status: Literal["positive_outlook", "negative_outlook", "stable", "uncertain"] = FieldInfo(
        alias="overallStatus"
    )
    """Overall assessment of the projected cash flow."""

    period: object
    """The period covered by the forecast."""

    projected_balances: List[ProjectedBalance] = FieldInfo(alias="projectedBalances")
    """Projected cash balances at key dates, potentially across different scenarios."""
