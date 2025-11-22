# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InternationalPaymentStatus"]


class InternationalPaymentStatus(BaseModel):
    fx_rate_applied: float = FieldInfo(alias="fxRateApplied")
    """The foreign exchange rate applied (targetCurrency per sourceCurrency)."""

    payment_id: str = FieldInfo(alias="paymentId")
    """Unique identifier for the international payment."""

    source_amount: float = FieldInfo(alias="sourceAmount")
    """The amount sent from the source account."""

    source_currency: str = FieldInfo(alias="sourceCurrency")
    """The currency from which funds were sent."""

    status: Literal["in_progress", "held_for_review", "completed", "failed", "cancelled"]
    """Current processing status of the international payment."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """The amount received by the beneficiary in the target currency."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The currency received by the beneficiary."""

    estimated_completion_time: Optional[datetime] = FieldInfo(alias="estimatedCompletionTime", default=None)
    """Estimated date and time for payment completion."""

    fees_applied: Optional[float] = FieldInfo(alias="feesApplied", default=None)
    """Any fees applied to the international payment."""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when the payment status was last updated."""

    message: Optional[str] = None
    """Additional messages, e.g., for held payments."""

    tracking_url: Optional[str] = FieldInfo(alias="trackingUrl", default=None)
    """URL to track the payment's progress."""
