# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxRetrieveRatesResponse", "CurrentRate", "HistoricalVolatility", "PredictiveRate"]


class CurrentRate(BaseModel):
    ask: Optional[float] = None

    bid: Optional[float] = None

    mid: Optional[float] = None

    timestamp: Optional[datetime.datetime] = None


class HistoricalVolatility(BaseModel):
    past30_days: Optional[float] = FieldInfo(alias="past30Days", default=None)

    past7_days: Optional[float] = FieldInfo(alias="past7Days", default=None)


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
    """Current real-time foreign exchange rates."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The target currency for the rate."""

    historical_volatility: Optional[HistoricalVolatility] = FieldInfo(alias="historicalVolatility", default=None)
    """Historical volatility metrics for the currency pair."""

    predictive_rates: Optional[List[PredictiveRate]] = FieldInfo(alias="predictiveRates", default=None)
    """AI-predicted foreign exchange rates for future dates with confidence intervals."""
