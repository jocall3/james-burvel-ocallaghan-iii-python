# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InternationalPaymentStatus"]


class InternationalPaymentStatus(BaseModel):
    fx_rate_applied: float = FieldInfo(alias="fxRateApplied")
    """The foreign exchange rate applied (target per source currency)."""

    payment_id: str = FieldInfo(alias="paymentId")
    """Unique identifier for the international payment."""

    source_amount: float = FieldInfo(alias="sourceAmount")
    """The amount sent in the source currency."""

    source_currency: str = FieldInfo(alias="sourceCurrency")
    """The source currency code."""

    status: Literal["in_progress", "held_for_review", "completed", "failed", "cancelled"]
    """Current processing status of the payment."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """The amount received by the beneficiary in the target currency."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The target currency code."""

    estimated_completion_time: Optional[datetime] = FieldInfo(alias="estimatedCompletionTime", default=None)
    """Estimated time when the payment will be completed."""

    fees_applied: Optional[float] = FieldInfo(alias="feesApplied", default=None)
    """Total fees applied to the payment."""

    message: Optional[str] = None
    """
    An optional message providing more context on the status (e.g., reason for
    hold).
    """

    tracking_url: Optional[str] = FieldInfo(alias="trackingUrl", default=None)
    """URL to track the payment's progress."""
