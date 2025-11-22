# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SustainabilityPurchaseCarbonOffsetsParams"]


class SustainabilityPurchaseCarbonOffsetsParams(TypedDict, total=False):
    amount_kg_co2e: Required[Annotated[float, PropertyInfo(alias="amountKgCO2e")]]
    """Amount of CO2 equivalent (in kilograms) to offset."""

    offset_project: Required[Annotated[str, PropertyInfo(alias="offsetProject")]]
    """The name or ID of the carbon offset project to support."""

    payment_account_id: Required[Annotated[str, PropertyInfo(alias="paymentAccountId")]]
    """The ID of the user's account to debit for the purchase."""

    auto_offset_monthly: Annotated[bool, PropertyInfo(alias="autoOffsetMonthly")]
    """If true, automatically purchase offsets monthly based on estimated footprint."""
