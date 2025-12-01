# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FxConvertResponse"]


class FxConvertResponse(BaseModel):
    conversion_id: object = FieldInfo(alias="conversionId")
    """Unique identifier for the currency conversion."""

    conversion_timestamp: object = FieldInfo(alias="conversionTimestamp")
    """Timestamp when the conversion was completed."""

    fx_rate_applied: object = FieldInfo(alias="fxRateApplied")
    """The foreign exchange rate applied (target per source currency)."""

    source_amount: object = FieldInfo(alias="sourceAmount")
    """The amount converted from the source currency."""

    source_currency: object = FieldInfo(alias="sourceCurrency")
    """The source currency code."""

    status: Literal["completed", "pending", "failed"]
    """Status of the currency conversion."""

    target_amount: object = FieldInfo(alias="targetAmount")
    """The amount converted into the target currency."""

    fees_applied: Optional[object] = FieldInfo(alias="feesApplied", default=None)
    """Any fees applied to the conversion."""

    target_currency: Optional[object] = FieldInfo(alias="targetCurrency", default=None)
    """The target currency code."""

    transaction_id: Optional[object] = FieldInfo(alias="transactionId", default=None)
    """The ID of the internal transaction representing this conversion."""
