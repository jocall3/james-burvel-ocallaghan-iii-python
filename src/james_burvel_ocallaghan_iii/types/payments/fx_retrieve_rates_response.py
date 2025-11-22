# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxRetrieveRatesResponse", "CurrentRate", "HistoricalVolatility", "PredictiveRate"]


class CurrentRate(BaseModel):
    ask: float
    """The ask price (rate at which you can buy base currency)."""

    bid: float
    """The bid price (rate at which you can sell base currency)."""

    mid: float
    """The mid-market rate."""

    timestamp: datetime.datetime
    """Timestamp of the current rate."""


class HistoricalVolatility(BaseModel):
    past30_days: Optional[float] = FieldInfo(alias="past30Days", default=None)
    """Average daily volatility over the past 30 days."""

    past7_days: Optional[float] = FieldInfo(alias="past7Days", default=None)
    """Average daily volatility over the past 7 days."""


class PredictiveRate(BaseModel):
    ai_model_confidence: Optional[float] = FieldInfo(alias="aiModelConfidence", default=None)

    confidence_interval_lower: Optional[float] = FieldInfo(alias="confidenceIntervalLower", default=None)

    confidence_interval_upper: Optional[float] = FieldInfo(alias="confidenceIntervalUpper", default=None)

    date: Optional[datetime.date] = None

    predicted_mid_rate: Optional[float] = FieldInfo(alias="predictedMidRate", default=None)


class FxRetrieveRatesResponse(BaseModel):
    base_currency: str = FieldInfo(alias="baseCurrency")
    """The base currency for the rate."""

    current_rate: CurrentRate = FieldInfo(alias="currentRate")
    """Real-time current foreign exchange rates."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The target currency for the rate."""

    historical_volatility: Optional[HistoricalVolatility] = FieldInfo(alias="historicalVolatility", default=None)
    """Historical volatility data for the currency pair."""

    predictive_rates: Optional[List[PredictiveRate]] = FieldInfo(alias="predictiveRates", default=None)
    """AI-predicted future foreign exchange rates."""
