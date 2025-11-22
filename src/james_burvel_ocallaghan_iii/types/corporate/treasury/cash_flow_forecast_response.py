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
    ai_confidence: Optional[float] = FieldInfo(alias="aiConfidence", default=None)
    """AI's confidence score for this inflow source."""

    amount: Optional[float] = None
    """Projected amount from this source."""

    source: Optional[str] = None
    """Source of inflow."""


class InflowForecast(BaseModel):
    by_source: List[InflowForecastBySource] = FieldInfo(alias="bySource")
    """Breakdown of inflows by source."""

    total_projected: float = FieldInfo(alias="totalProjected")
    """Total projected inflows."""


class OutflowForecastByCategory(BaseModel):
    ai_confidence: Optional[float] = FieldInfo(alias="aiConfidence", default=None)
    """AI's confidence score for this outflow category."""

    amount: Optional[float] = None
    """Projected amount for this category."""

    category: Optional[str] = None
    """Category of outflow."""


class OutflowForecast(BaseModel):
    by_category: List[OutflowForecastByCategory] = FieldInfo(alias="byCategory")
    """Breakdown of outflows by category."""

    total_projected: float = FieldInfo(alias="totalProjected")
    """Total projected outflows."""


class ProjectedBalance(BaseModel):
    date: datetime.date
    """Date of the projected balance."""

    projected_cash: float = FieldInfo(alias="projectedCash")
    """Projected cash balance on this date."""

    scenario: Literal["most_likely", "best_case", "worst_case", "custom"]
    """The scenario for this projection."""


class CashFlowForecastResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-generated recommendations for treasury optimization."""

    currency: str
    """The primary currency of the forecast."""

    forecast_id: str = FieldInfo(alias="forecastId")
    """Unique identifier for the cash flow forecast."""

    inflow_forecast: InflowForecast = FieldInfo(alias="inflowForecast")
    """Forecasted cash inflows."""

    liquidity_risk_score: int = FieldInfo(alias="liquidityRiskScore")
    """AI-assessed score for liquidity risk (0-100, higher is riskier)."""

    outflow_forecast: OutflowForecast = FieldInfo(alias="outflowForecast")
    """Forecasted cash outflows."""

    overall_status: Literal["positive_outlook", "neutral", "potential_deficit", "critical_risk"] = FieldInfo(
        alias="overallStatus"
    )
    """Overall assessment of the cash flow outlook."""

    period: str
    """The period covered by the forecast."""

    projected_balances: List[ProjectedBalance] = FieldInfo(alias="projectedBalances")
    """Time-series of projected cash balances under different scenarios."""

    forecast_timestamp: Optional[datetime.datetime] = FieldInfo(alias="forecastTimestamp", default=None)
    """Timestamp when the forecast was generated."""

    scenario_analysis_summary: Optional[str] = FieldInfo(alias="scenarioAnalysisSummary", default=None)
    """Summary of 'what-if' scenario analysis included in the forecast."""
