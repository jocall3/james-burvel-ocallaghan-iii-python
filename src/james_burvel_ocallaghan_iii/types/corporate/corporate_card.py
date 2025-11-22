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
    """Masked card number for display."""

    card_type: Literal["physical", "virtual"] = FieldInfo(alias="cardType")
    """Type of card (physical or virtual)."""

    controls: CorporateCardControls
    """Granular spending controls applied to this card."""

    created_date: datetime = FieldInfo(alias="createdDate")
    """Date and time the card was created."""

    expiration_date: date = FieldInfo(alias="expirationDate")
    """Card expiration date."""

    frozen: bool
    """True if the card is temporarily frozen and cannot be used."""

    holder_name: str = FieldInfo(alias="holderName")
    """Name of the cardholder (employee or campaign name)."""

    status: Literal["Active", "Suspended", "Deactivated", "Expired"]
    """Current status of the card."""

    associated_employee_id: Optional[str] = FieldInfo(alias="associatedEmployeeId", default=None)
    """Optional: Employee ID if associated with a specific individual."""

    spending_policy_id: Optional[str] = FieldInfo(alias="spendingPolicyId", default=None)
    """Optional: ID of the overarching corporate spending policy this card adheres to."""

    usage_purpose: Optional[str] = FieldInfo(alias="usagePurpose", default=None)
    """A description of the card's intended use or purpose."""
