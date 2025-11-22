# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .corporate_card_controls_param import CorporateCardControlsParam

__all__ = ["CardCreateVirtualParams"]


class CardCreateVirtualParams(TypedDict, total=False):
    controls: Required[CorporateCardControlsParam]
    """Specific spending controls for this virtual card."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]]
    """The expiration date for the virtual card."""

    holder_name: Required[Annotated[str, PropertyInfo(alias="holderName")]]
    """Name for the virtual card holder (can be a campaign, project, or individual)."""

    purpose: Required[str]
    """Clear purpose of the virtual card's use."""

    associated_employee_id: Annotated[Optional[str], PropertyInfo(alias="associatedEmployeeId")]
    """Optional: Employee ID if associated with an individual."""
