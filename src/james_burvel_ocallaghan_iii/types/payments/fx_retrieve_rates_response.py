# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxRetrieveRatesResponse", "CurrentRate", "HistoricalVolatility", "PredictiveRate"]


class CurrentRate(BaseModel):
    ask: Optional[float] = None
    """
    Current ask rate (price at which a currency dealer will sell the base currency).
    """

    bid: Optional[float] = None
    """Current bid rate (price at which a currency dealer will buy the base currency)."""

    mid: Optional[float] = None
    """Mid-market rate (average of bid and ask)."""

    timestamp: Optional[datetime.datetime] = None
    """Timestamp of the current rate."""


class HistoricalVolatility(BaseModel):
    past30_days: Optional[float] = FieldInfo(alias="past30Days", default=None)
    """Historical volatility over the past 30 days."""

    past7_days: Optional[float] = FieldInfo(alias="past7Days", default=None)
    """Historical volatility over the past 7 days."""


class PredictiveRate(BaseModel):
    ai_model_confidence: Optional[float] = FieldInfo(alias="aiModelConfidence", default=None)
    """AI model's confidence in the prediction (0-1)."""

    confidence_interval_lower: Optional[float] = FieldInfo(alias="confidenceIntervalLower", default=None)
    """Lower bound of the AI's confidence interval for the predicted rate."""

    confidence_interval_upper: Optional[float] = FieldInfo(alias="confidenceIntervalUpper", default=None)
    """Upper bound of the AI's confidence interval for the predicted rate."""

    date: Optional[datetime.date] = None
    """Date for the predicted rate."""

    predicted_mid_rate: Optional[float] = FieldInfo(alias="predictedMidRate", default=None)
    """AI-predicted mid-market rate."""


class FxRetrieveRatesResponse(BaseModel):
    base_currency: str = FieldInfo(alias="baseCurrency")
    """The base currency code."""

    current_rate: CurrentRate = FieldInfo(alias="currentRate")
    """Real-time foreign exchange rates."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The target currency code."""

    historical_volatility: Optional[HistoricalVolatility] = FieldInfo(alias="historicalVolatility", default=None)

    predictive_rates: Optional[List[PredictiveRate]] = FieldInfo(alias="predictiveRates", default=None)
    """AI-predicted foreign exchange rates for future dates."""
