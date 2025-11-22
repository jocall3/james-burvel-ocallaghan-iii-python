# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductClaimOfferResponse"]


class ProductClaimOfferResponse(BaseModel):
    message: str
    """A confirmation message with redemption instructions."""

    offer_id: str = FieldInfo(alias="offerId")
    """Unique identifier for the claimed offer."""

    product_id: str = FieldInfo(alias="productId")
    """The ID of the product related to the offer."""

    status: Literal["claimed", "redeemed", "expired", "cancelled"]
    """Current status of the offer."""

    claim_date: Optional[datetime] = FieldInfo(alias="claimDate", default=None)
    """Timestamp when the offer was claimed."""

    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """The date and time the offer expires."""

    redemption_code: Optional[str] = FieldInfo(alias="redemptionCode", default=None)
    """The code needed to redeem the offer, if applicable."""

    redemption_link: Optional[str] = FieldInfo(alias="redemptionLink", default=None)
    """A direct link to redeem the offer, if applicable."""
