# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SustainabilityPurchaseCarbonOffsetsParams"]


class SustainabilityPurchaseCarbonOffsetsParams(TypedDict, total=False):
    amount_kg_co2e: Required[Annotated[float, PropertyInfo(alias="amountKgCO2e")]]
    """The amount of carbon (in Kg CO2e) to offset."""

    offset_project: Required[Annotated[Optional[str], PropertyInfo(alias="offsetProject")]]
    """Optional: Name or ID of a preferred carbon offset project.

    If null, AI will select an optimal project.
    """

    payment_account_id: Required[Annotated[str, PropertyInfo(alias="paymentAccountId")]]
    """The ID of the user's account to debit for the purchase."""

    recurring: bool
    """If true, sets up a recurring carbon offset purchase."""
