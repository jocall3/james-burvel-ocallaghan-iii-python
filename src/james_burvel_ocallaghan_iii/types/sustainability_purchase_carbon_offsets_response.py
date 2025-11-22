# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SustainabilityPurchaseCarbonOffsetsResponse"]


class SustainabilityPurchaseCarbonOffsetsResponse(BaseModel):
    amount_offset_kg_co2e: float = FieldInfo(alias="amountOffsetKgCO2e")
    """The amount of carbon (in Kg CO2e) that was offset."""

    project_supported: str = FieldInfo(alias="projectSupported")
    """The name of the carbon offset project supported."""

    purchase_date: datetime = FieldInfo(alias="purchaseDate")
    """Date and time of the offset purchase."""

    purchase_id: str = FieldInfo(alias="purchaseId")
    """Unique identifier for the carbon offset purchase."""

    total_cost_usd: float = FieldInfo(alias="totalCostUSD")
    """The total cost of the carbon offset purchase in USD."""

    certificate_url: Optional[str] = FieldInfo(alias="certificateUrl", default=None)
    """URL to the carbon offset certificate."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """The ID of the associated financial transaction."""
