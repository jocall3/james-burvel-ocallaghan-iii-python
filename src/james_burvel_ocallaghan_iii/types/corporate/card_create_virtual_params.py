# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .corporate_card_controls_param import CorporateCardControlsParam

__all__ = ["CardCreateVirtualParams"]


class CardCreateVirtualParams(TypedDict, total=False):
    controls: Required[CorporateCardControlsParam]
    """Granular spending controls for a corporate card."""

    expiration_date: Required[Annotated[object, PropertyInfo(alias="expirationDate")]]
    """Expiration date for the virtual card (YYYY-MM-DD)."""

    holder_name: Required[Annotated[object, PropertyInfo(alias="holderName")]]
    """Name to appear on the virtual card."""

    purpose: Required[object]
    """Brief description of the virtual card's purpose."""

    associated_employee_id: Annotated[object, PropertyInfo(alias="associatedEmployeeId")]
    """Optional: ID of the employee or department this card is for."""

    spending_policy_id: Annotated[object, PropertyInfo(alias="spendingPolicyId")]
    """Optional: ID of a spending policy to link with this virtual card."""
