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

    fx_rate_applied: float = FieldInfo(alias="fxRateApplied")
    """The foreign exchange rate applied (targetCurrency per sourceCurrency)."""

    source_amount: float = FieldInfo(alias="sourceAmount")
    """Amount converted from the source currency."""

    source_currency: str = FieldInfo(alias="sourceCurrency")
    """Source currency of the conversion."""

    status: Literal["completed", "failed"]
    """Status of the currency conversion."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """Amount received in the target currency."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """
    The transaction ID associated with the conversion in the user's account history.
    """

    fees_applied: Optional[float] = FieldInfo(alias="feesApplied", default=None)
    """Any fees applied to the conversion."""
