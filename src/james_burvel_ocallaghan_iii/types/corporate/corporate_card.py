# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .corporate_card_controls import CorporateCardControls

__all__ = ["CorporateCard"]


class CorporateCard(BaseModel):
    id: object
    """Unique identifier for the corporate card."""

    card_number_mask: object = FieldInfo(alias="cardNumberMask")
    """Masked card number for display purposes."""

    card_type: Literal["physical", "virtual"] = FieldInfo(alias="cardType")
    """Type of the card (physical or virtual)."""

    controls: CorporateCardControls
    """Granular spending controls for a corporate card."""

    created_date: object = FieldInfo(alias="createdDate")
    """Timestamp when the card was created."""

    currency: object
    """Currency of the card's limits and transactions."""

    expiration_date: object = FieldInfo(alias="expirationDate")
    """Expiration date of the card (YYYY-MM-DD)."""

    frozen: object
    """If true, the card is temporarily frozen and cannot be used."""

    holder_name: object = FieldInfo(alias="holderName")
    """Name of the card holder."""

    status: Literal["Active", "Suspended", "Deactivated", "Pending Activation"]
    """Current status of the card."""

    associated_employee_id: Optional[object] = FieldInfo(alias="associatedEmployeeId", default=None)
    """Optional: ID of the employee associated with this card."""

    spending_policy_id: Optional[object] = FieldInfo(alias="spendingPolicyId", default=None)
    """Optional: ID of the overarching spending policy applied to this card."""
