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
    """Masked card number for display (e.g., last 4 digits)."""

    card_type: Literal["physical", "virtual"] = FieldInfo(alias="cardType")
    """Type of card (physical or virtual)."""

    controls: CorporateCardControls
    """Granular spending controls and limits for the card."""

    created_date: datetime = FieldInfo(alias="createdDate")
    """Date when the card was created/issued."""

    expiration_date: date = FieldInfo(alias="expirationDate")
    """Expiration date of the card."""

    frozen: bool
    """Indicates if the card is temporarily frozen (no transactions allowed)."""

    holder_name: str = FieldInfo(alias="holderName")
    """Name of the employee or entity holding the card."""

    status: Literal["Active", "Suspended", "Cancelled", "Expired"]
    """Current status of the card."""

    associated_employee_id: Optional[str] = FieldInfo(alias="associatedEmployeeId", default=None)
    """Optional: ID of the employee associated with the card."""

    currency: Optional[str] = None
    """The primary currency of the card."""

    spending_policy_id: Optional[str] = FieldInfo(alias="spendingPolicyId", default=None)
    """Optional: ID of the corporate spending policy this card adheres to."""
