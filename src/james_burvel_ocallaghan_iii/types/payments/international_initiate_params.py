# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InternationalInitiateParams", "Beneficiary"]


class InternationalInitiateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of money to send in the `sourceCurrency`."""

    beneficiary: Required[Beneficiary]
    """Details of the recipient for the international payment."""

    purpose: Required[str]
    """A clear and concise purpose for the payment."""

    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the source account from which funds will be sent."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The currency of the source account (ISO 4217 code)."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The target currency for the beneficiary (ISO 4217 code)."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the FX rate at the time of initiation."""

    fx_rate_provider: Annotated[
        Optional[Literal["proprietary_ai", "market", "partner_bank"]], PropertyInfo(alias="fxRateProvider")
    ]
    """Optional: Preferred FX rate provider for the conversion."""

    reference_id: Annotated[Optional[str], PropertyInfo(alias="referenceId")]
    """Optional: An external reference ID for this payment."""


class Beneficiary(TypedDict, total=False):
    address: Required[str]
    """Full address of the beneficiary."""

    bank_name: Required[Annotated[str, PropertyInfo(alias="bankName")]]
    """Name of the beneficiary's bank."""

    iban: Required[str]
    """International Bank Account Number (IBAN) of the beneficiary."""

    name: Required[str]
    """Full name of the beneficiary."""

    swift_bic: Required[Annotated[str, PropertyInfo(alias="swiftBic")]]
    """SWIFT/BIC code of the beneficiary's bank."""

    account_number: Annotated[Optional[str], PropertyInfo(alias="accountNumber")]
    """Optional: Traditional bank account number if IBAN not applicable."""
