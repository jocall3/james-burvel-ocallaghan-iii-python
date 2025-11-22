# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductClaimOfferResponse"]


class ProductClaimOfferResponse(BaseModel):
    message: str
    """A descriptive message for the user about the claimed offer."""

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the claimed offer."""

    product_id: str = FieldInfo(alias="productId")
    """The ID of the product the offer applies to."""

    status: Literal["claimed", "redeemed", "expired"]
    """Current status of the offer."""

    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """The date and time when the offer expires."""

    redemption_code: Optional[str] = FieldInfo(alias="redemptionCode", default=None)
    """A code to be used for redemption (if applicable)."""

    redemption_link: Optional[str] = FieldInfo(alias="redemptionLink", default=None)
    """A direct link for redeeming the offer (if applicable)."""
