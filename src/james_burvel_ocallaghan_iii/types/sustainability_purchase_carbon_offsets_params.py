# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SustainabilityPurchaseCarbonOffsetsParams"]


class SustainabilityPurchaseCarbonOffsetsParams(TypedDict, total=False):
    amount_kg_co2e: Required[Annotated[float, PropertyInfo(alias="amountKgCO2e")]]
    """The amount of carbon (in Kg CO2e) to offset."""

    payment_account_id: Required[Annotated[str, PropertyInfo(alias="paymentAccountId")]]
    """The ID of the account to use for payment."""

    offset_project: Annotated[Optional[str], PropertyInfo(alias="offsetProject")]
    """Optional: A specific carbon offset project or standard to support."""
