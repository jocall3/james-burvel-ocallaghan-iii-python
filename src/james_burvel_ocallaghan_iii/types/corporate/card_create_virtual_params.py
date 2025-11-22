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
    """Specific spending controls and limits for this virtual card."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]]
    """Expiration date of the virtual card."""

    holder_name: Required[Annotated[str, PropertyInfo(alias="holderName")]]
    """Name of the entity or campaign for which the virtual card is issued."""

    purpose: Required[str]
    """The purpose or use case for this virtual card."""

    associated_employee_id: Annotated[Optional[str], PropertyInfo(alias="associatedEmployeeId")]
    """Optional: ID of the employee responsible for this virtual card."""

    currency: str
    """The primary currency of the virtual card."""
