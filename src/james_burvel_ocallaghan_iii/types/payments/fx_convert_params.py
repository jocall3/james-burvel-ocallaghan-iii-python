# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FxConvertParams"]


class FxConvertParams(TypedDict, total=False):
    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the account from which to convert funds."""

    source_amount: Required[Annotated[float, PropertyInfo(alias="sourceAmount")]]
    """The amount to convert from the source currency."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The currency to convert from (ISO 4217 code)."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The currency to convert to (ISO 4217 code)."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the FX rate at the time of conversion."""

    target_account_id: Annotated[Optional[str], PropertyInfo(alias="targetAccountId")]
    """Optional: The ID of the target account to deposit converted funds.

    If omitted, converted funds will be deposited back to sourceAccountId (if
    multi-currency capable) or a default linked account.
    """
