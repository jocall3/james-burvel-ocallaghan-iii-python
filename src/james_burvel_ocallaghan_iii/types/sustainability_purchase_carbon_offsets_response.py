# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SustainabilityPurchaseCarbonOffsetsResponse"]


class SustainabilityPurchaseCarbonOffsetsResponse(BaseModel):
    amount_offset_kg_co2e: float = FieldInfo(alias="amountOffsetKgCO2e")
    """The amount of carbon dioxide equivalent offset by this purchase."""

    purchase_date: datetime = FieldInfo(alias="purchaseDate")
    """Timestamp of the purchase."""

    purchase_id: str = FieldInfo(alias="purchaseId")
    """Unique identifier for the carbon offset purchase."""

    total_cost_usd: float = FieldInfo(alias="totalCostUSD")
    """Total cost of the carbon offset purchase in USD."""

    certificate_url: Optional[str] = FieldInfo(alias="certificateUrl", default=None)
    """URL to the official carbon offset certificate."""

    project_supported: Optional[str] = FieldInfo(alias="projectSupported", default=None)
    """The carbon offset project supported."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """The ID of the internal financial transaction for this purchase."""
