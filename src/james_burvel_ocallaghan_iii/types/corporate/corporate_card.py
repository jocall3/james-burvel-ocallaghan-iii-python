# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .corporate_card_controls import CorporateCardControls

__all__ = ["CorporateCard"]


class CorporateCard(BaseModel):
    id: str
    """Unique identifier for the corporate card."""

    card_number_mask: str = FieldInfo(alias="cardNumberMask")
    """Masked card number for display purposes."""

    card_type: Literal["physical", "virtual"] = FieldInfo(alias="cardType")
    """Type of the corporate card."""

    controls: CorporateCardControls
    """Granular spending controls applied to this card."""

    created_date: datetime = FieldInfo(alias="createdDate")
    """Date when the card was created/issued."""

    expiration_date: date = FieldInfo(alias="expirationDate")
    """Expiration date of the card."""

    frozen: bool
    """True if the card is currently frozen, preventing transactions."""

    holder_name: str = FieldInfo(alias="holderName")
    """Name of the cardholder or purpose."""

    status: Literal["Active", "Suspended", "Cancelled", "Expired"]
    """Current status of the card."""

    associated_employee_id: Optional[str] = FieldInfo(alias="associatedEmployeeId", default=None)
    """Employee ID associated with the card (if applicable)."""

    spending_policy_id: Optional[str] = FieldInfo(alias="spendingPolicyId", default=None)
    """ID of the corporate spending policy this card adheres to (if any)."""
