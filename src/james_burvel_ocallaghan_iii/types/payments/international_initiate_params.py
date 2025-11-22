# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InternationalInitiateParams", "Beneficiary"]


class InternationalInitiateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to send from the source account in `sourceCurrency`."""

    beneficiary: Required[Beneficiary]
    """Details of the recipient for the international payment."""

    purpose: Required[str]
    """A short description or purpose for the payment."""

    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the user's account from which funds will be sent."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The currency of the source account (ISO 4217 code)."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The currency the beneficiary will receive (ISO 4217 code)."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the quoted FX rate. May incur a small fee."""

    fx_rate_provider: Annotated[
        Literal["proprietary_ai", "standard_interbank", "third_party"], PropertyInfo(alias="fxRateProvider")
    ]
    """Preferred FX rate provider for the conversion."""

    reference_id: Annotated[Optional[str], PropertyInfo(alias="referenceId")]
    """Optional: An internal reference ID or invoice number for the payment."""


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
    """Optional: Traditional bank account number if IBAN is not applicable."""

    routing_number: Annotated[Optional[str], PropertyInfo(alias="routingNumber")]
    """Optional: Routing number for US beneficiaries."""
