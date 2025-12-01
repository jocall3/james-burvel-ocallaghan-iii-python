# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FxRetrieveRatesParams"]


class FxRetrieveRatesParams(TypedDict, total=False):
    base_currency: Required[Annotated[object, PropertyInfo(alias="baseCurrency")]]
    """The base currency code (e.g., USD)."""

    target_currency: Required[Annotated[object, PropertyInfo(alias="targetCurrency")]]
    """The target currency code (e.g., EUR)."""

    forecast_days: Annotated[object, PropertyInfo(alias="forecastDays")]
    """Number of days into the future to provide an AI-driven prediction."""
