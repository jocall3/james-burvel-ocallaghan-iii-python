# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxRetrieveRatesResponse", "CurrentRate", "AIRiskAssessment", "HistoricalVolatility", "PredictiveRate"]


class CurrentRate(BaseModel):
    ask: float
    """The ask price (rate at which the market will sell the base currency)."""

    bid: float
    """The bid price (rate at which the market will buy the base currency)."""

    mid: float
    """The mid-market rate (average of bid and ask)."""

    timestamp: datetime.datetime
    """Timestamp of the rate quote."""


class AIRiskAssessment(BaseModel):
    event_risk_factors: Optional[List[str]] = FieldInfo(alias="eventRiskFactors", default=None)
    """AI-identified events that could impact FX rates."""

    volatility_forecast: Optional[Literal["low", "medium", "high"]] = FieldInfo(
        alias="volatilityForecast", default=None
    )
    """AI forecast for future volatility."""


class HistoricalVolatility(BaseModel):
    past30_days: Optional[float] = FieldInfo(alias="past30Days", default=None)
    """Volatility over the past 30 days."""

    past7_days: Optional[float] = FieldInfo(alias="past7Days", default=None)
    """Volatility over the past 7 days."""


class PredictiveRate(BaseModel):
    ai_model_confidence: float = FieldInfo(alias="aiModelConfidence")
    """AI model's confidence (0-1) in this specific prediction."""

    confidence_interval_lower: float = FieldInfo(alias="confidenceIntervalLower")
    """Lower bound of the confidence interval for the prediction."""

    confidence_interval_upper: float = FieldInfo(alias="confidenceIntervalUpper")
    """Upper bound of the confidence interval for the prediction."""

    date: datetime.date
    """The date for which the rate is predicted."""

    predicted_mid_rate: float = FieldInfo(alias="predictedMidRate")
    """The AI's predicted mid-market rate for that date."""


class FxRetrieveRatesResponse(BaseModel):
    base_currency: str = FieldInfo(alias="baseCurrency")
    """The base currency code."""

    current_rate: CurrentRate = FieldInfo(alias="currentRate")
    """The current real-time exchange rates."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The target currency code."""

    ai_risk_assessment: Optional[AIRiskAssessment] = FieldInfo(alias="aiRiskAssessment", default=None)
    """AI-driven risk assessment for the currency pair."""

    historical_volatility: Optional[HistoricalVolatility] = FieldInfo(alias="historicalVolatility", default=None)
    """Historical volatility data for the currency pair."""

    predictive_rates: Optional[List[PredictiveRate]] = FieldInfo(alias="predictiveRates", default=None)
    """AI-predicted future exchange rates for the specified forecast horizon."""
