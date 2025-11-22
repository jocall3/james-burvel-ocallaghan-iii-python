# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FxConvertParams"]


class FxConvertParams(TypedDict, total=False):
    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the user's account from which funds will be converted."""

    source_amount: Required[Annotated[float, PropertyInfo(alias="sourceAmount")]]
    """The amount to convert from the source account in `sourceCurrency`."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The currency to convert from (ISO 4217 code)."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The currency to convert to (ISO 4217 code)."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the quoted FX rate. May incur a small fee."""

    fx_rate_provider: Annotated[
        Literal["proprietary_ai", "standard_interbank", "third_party"], PropertyInfo(alias="fxRateProvider")
    ]
    """Preferred FX rate provider for the conversion."""

    target_account_id: Annotated[Optional[str], PropertyInfo(alias="targetAccountId")]
    """Optional: The ID of the target account to receive the converted funds.

    If omitted, funds are converted within the source account's currency
    capabilities or a new balance is created.
    """
