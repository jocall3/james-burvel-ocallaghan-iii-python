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
    """Details of the international beneficiary."""

    purpose: Required[str]
    """Purpose of the payment (e.g., invoice payment, family support)."""

    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The ID of the local account from which funds will be sent."""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The currency of the source account."""

    target_currency: Required[Annotated[str, PropertyInfo(alias="targetCurrency")]]
    """The desired currency for the beneficiary."""

    fx_rate_lock: Annotated[bool, PropertyInfo(alias="fxRateLock")]
    """If true, attempts to lock the quoted FX rate for the transaction."""

    fx_rate_provider: Annotated[
        Literal["proprietary_ai", "external_partner", "market_rate"], PropertyInfo(alias="fxRateProvider")
    ]
    """The desired provider for the foreign exchange rate."""

    reference_number: Annotated[Optional[str], PropertyInfo(alias="referenceNumber")]
    """Optional reference number for the payment (e.g., invoice number)."""


class Beneficiary(TypedDict, total=False):
    address: Required[str]

    bank_name: Required[Annotated[str, PropertyInfo(alias="bankName")]]

    iban: Required[str]

    name: Required[str]

    swift_bic: Required[Annotated[str, PropertyInfo(alias="swiftBic")]]
