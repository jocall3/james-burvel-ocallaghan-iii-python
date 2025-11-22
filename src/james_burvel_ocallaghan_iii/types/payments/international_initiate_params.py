# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InternationalInitiateParams", "Beneficiary"]


class InternationalInitiateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to send in the source currency."""

    beneficiary: Required[Beneficiary]
    """Details of the payment beneficiary."""

    purpose: Required[str]
    """Purpose of the payment."""

    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the user's source account for the payment."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The ISO 4217 currency code of the source funds."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The ISO 4217 currency code for the beneficiary's currency."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the quoted FX rate for a short period."""

    fx_rate_provider: Annotated[Literal["proprietary_ai", "market_rate"], PropertyInfo(alias="fxRateProvider")]
    """Indicates whether to use AI-optimized FX rates or standard market rates."""

    reference: Optional[str]
    """Optional: Your internal reference for this payment."""


class Beneficiary(TypedDict, total=False):
    address: Required[str]
    """Full address of the beneficiary."""

    bank_name: Required[Annotated[str, PropertyInfo(alias="bankName")]]
    """Name of the beneficiary's bank."""

    name: Required[str]
    """Full name of the beneficiary."""

    account_number: Annotated[Optional[str], PropertyInfo(alias="accountNumber")]
    """Account number (if IBAN/SWIFT not applicable)."""

    iban: Optional[str]
    """IBAN for Eurozone transfers."""

    routing_number: Annotated[Optional[str], PropertyInfo(alias="routingNumber")]
    """Routing number (if applicable, e.g., for US transfers)."""

    swift_bic: Annotated[Optional[str], PropertyInfo(alias="swiftBic")]
    """SWIFT/BIC code for international transfers."""
