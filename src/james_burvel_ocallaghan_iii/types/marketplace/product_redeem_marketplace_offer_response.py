# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductRedeemMarketplaceOfferResponse"]


class ProductRedeemMarketplaceOfferResponse(BaseModel):
    associated_transaction_id: Optional[object] = FieldInfo(alias="associatedTransactionId", default=None)
    """
    If applicable, the ID of any associated transaction (e.g., a credit or initial
    payment).
    """

    message: Optional[object] = None
    """A descriptive message about the redemption."""

    offer_id: Optional[object] = FieldInfo(alias="offerId", default=None)
    """The ID of the redeemed offer."""

    redemption_date: Optional[object] = FieldInfo(alias="redemptionDate", default=None)

    redemption_id: Optional[object] = FieldInfo(alias="redemptionId", default=None)
    """Unique ID for this redemption."""

    status: Optional[Literal["success", "pending", "failed"]] = None
    """Status of the redemption."""
