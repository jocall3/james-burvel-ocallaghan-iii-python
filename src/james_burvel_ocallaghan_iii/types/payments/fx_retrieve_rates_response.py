# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxRetrieveRatesResponse", "CurrentRate", "HistoricalVolatility", "PredictiveRate"]


class CurrentRate(BaseModel):
    ask: Optional[object] = None
    """
    Current ask rate (price at which a currency dealer will sell the base currency).
    """

    bid: Optional[object] = None
    """Current bid rate (price at which a currency dealer will buy the base currency)."""

    mid: Optional[object] = None
    """Mid-market rate (average of bid and ask)."""

    timestamp: Optional[object] = None
    """Timestamp of the current rate."""


class HistoricalVolatility(BaseModel):
    past30_days: Optional[object] = FieldInfo(alias="past30Days", default=None)
    """Historical volatility over the past 30 days."""

    past7_days: Optional[object] = FieldInfo(alias="past7Days", default=None)
    """Historical volatility over the past 7 days."""


class PredictiveRate(BaseModel):
    ai_model_confidence: Optional[object] = FieldInfo(alias="aiModelConfidence", default=None)
    """AI model's confidence in the prediction (0-1)."""

    confidence_interval_lower: Optional[object] = FieldInfo(alias="confidenceIntervalLower", default=None)
    """Lower bound of the AI's confidence interval for the predicted rate."""

    confidence_interval_upper: Optional[object] = FieldInfo(alias="confidenceIntervalUpper", default=None)
    """Upper bound of the AI's confidence interval for the predicted rate."""

    date: Optional[object] = None
    """Date for the predicted rate."""

    predicted_mid_rate: Optional[object] = FieldInfo(alias="predictedMidRate", default=None)
    """AI-predicted mid-market rate."""


class FxRetrieveRatesResponse(BaseModel):
    base_currency: object = FieldInfo(alias="baseCurrency")
    """The base currency code."""

    current_rate: CurrentRate = FieldInfo(alias="currentRate")
    """Real-time foreign exchange rates."""

    target_currency: object = FieldInfo(alias="targetCurrency")
    """The target currency code."""

    historical_volatility: Optional[HistoricalVolatility] = FieldInfo(alias="historicalVolatility", default=None)

    predictive_rates: Optional[List[PredictiveRate]] = FieldInfo(alias="predictiveRates", default=None)
    """AI-predicted foreign exchange rates for future dates."""
