# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductClaimOfferResponse"]


class ProductClaimOfferResponse(BaseModel):
    message: str
    """A message providing redemption instructions or confirmation."""

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the claimed offer."""

    product_id: str = FieldInfo(alias="productId")
    """The ID of the product related to the offer."""

    status: Literal["claimed", "redeemed", "expired"]
    """Current status of the offer."""

    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """Date and time when the claimed offer expires."""

    redemption_code: Optional[str] = FieldInfo(alias="redemptionCode", default=None)
    """Optional: A code needed to redeem the offer."""

    redemption_link: Optional[str] = FieldInfo(alias="redemptionLink", default=None)
    """Optional: A direct link to redeem the offer."""
