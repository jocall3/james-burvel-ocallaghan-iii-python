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
    """Expiration date for the virtual card."""

    holder_name: Required[Annotated[str, PropertyInfo(alias="holderName")]]
    """Name for the virtual card holder or its purpose."""

    purpose: Required[str]
    """Brief description of the virtual card's intended use."""

    associated_employee_id: Annotated[Optional[str], PropertyInfo(alias="associatedEmployeeId")]
    """Optional: Employee ID to associate with this virtual card."""
