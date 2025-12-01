# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FxConvertParams"]


class FxConvertParams(TypedDict, total=False):
    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the account from which funds will be converted."""

    source_amount: Required[Annotated[float, PropertyInfo(alias="sourceAmount")]]
    """The amount to convert from the source currency."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The ISO 4217 currency code of the source funds."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The ISO 4217 currency code for the target currency."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the quoted FX rate for a short period."""

    target_account_id: Annotated[Optional[str], PropertyInfo(alias="targetAccountId")]
    """Optional: The ID of the account to deposit the converted funds.

    If null, funds are held in a wallet/balance.
    """
