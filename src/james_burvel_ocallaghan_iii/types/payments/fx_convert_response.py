# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxConvertResponse"]


class FxConvertResponse(BaseModel):
    conversion_id: str = FieldInfo(alias="conversionId")
    """Unique identifier for the currency conversion."""

    conversion_timestamp: datetime = FieldInfo(alias="conversionTimestamp")
    """Timestamp when the conversion was completed."""

    fees_applied: float = FieldInfo(alias="feesApplied")
    """Total fees applied to the conversion."""

    fx_rate_applied: float = FieldInfo(alias="fxRateApplied")
    """The foreign exchange rate applied (target_currency / source_currency)."""

    source_amount: float = FieldInfo(alias="sourceAmount")
    """Amount converted from the source currency."""

    source_currency: str = FieldInfo(alias="sourceCurrency")
    """Currency of the source amount."""

    status: Literal["completed", "failed", "cancelled"]
    """Status of the currency conversion."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """Amount received in the target currency."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """Associated transaction ID in the user's account history."""
