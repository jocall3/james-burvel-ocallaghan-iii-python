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
    """Timestamp of the conversion."""

    fees_applied: float = FieldInfo(alias="feesApplied")
    """Any fees charged for the conversion."""

    fx_rate_applied: float = FieldInfo(alias="fxRateApplied")
    """The exchange rate applied (targetCurrency / sourceCurrency)."""

    source_amount: float = FieldInfo(alias="sourceAmount")
    """Amount of source currency converted."""

    source_currency: str = FieldInfo(alias="sourceCurrency")
    """Source currency code."""

    status: Literal["completed", "pending_review", "failed"]
    """Status of the currency conversion."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """Amount of target currency received."""

    target_currency: Optional[str] = FieldInfo(alias="targetCurrency", default=None)
    """Target currency code."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """The ID of the internal transaction recording the conversion."""
