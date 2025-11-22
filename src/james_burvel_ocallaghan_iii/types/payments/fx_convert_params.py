# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FxConvertParams"]


class FxConvertParams(TypedDict, total=False):
    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the account from which to deduct the source amount."""

    source_amount: Required[Annotated[float, PropertyInfo(alias="sourceAmount")]]
    """The amount to convert from the source currency."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The currency to convert from."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The currency to convert to."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the quoted FX rate for the conversion."""

    fx_rate_provider: Annotated[
        Literal["proprietary_ai", "external_partner", "market_rate"], PropertyInfo(alias="fxRateProvider")
    ]
    """The desired provider for the foreign exchange rate."""

    target_account_id: Annotated[Optional[str], PropertyInfo(alias="targetAccountId")]
    """Optional: The ID of the account to credit with the converted target amount.

    If omitted, converted funds remain as a floating balance or are deposited into a
    primary account.
    """
