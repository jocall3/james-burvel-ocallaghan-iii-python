# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SustainabilityPurchaseCarbonOffsetsParams"]


class SustainabilityPurchaseCarbonOffsetsParams(TypedDict, total=False):
    amount_kg_co2e: Required[Annotated[float, PropertyInfo(alias="amountKgCO2e")]]
    """The amount of carbon dioxide equivalent to offset in kilograms."""

    offset_project: Required[Annotated[Optional[str], PropertyInfo(alias="offsetProject")]]
    """Optional: The specific carbon offset project to support."""

    payment_account_id: Required[Annotated[str, PropertyInfo(alias="paymentAccountId")]]
    """The ID of the user's account to use for payment."""
