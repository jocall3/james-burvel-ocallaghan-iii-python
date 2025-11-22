# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InternationalPaymentStatus"]


class InternationalPaymentStatus(BaseModel):
    fees_applied: float = FieldInfo(alias="feesApplied")
    """Total fees applied to the payment."""

    fx_rate_applied: float = FieldInfo(alias="fxRateApplied")
    """The foreign exchange rate applied (targetCurrency / sourceCurrency)."""

    payment_id: str = FieldInfo(alias="paymentId")
    """Unique identifier for the international payment."""

    source_amount: float = FieldInfo(alias="sourceAmount")
    """The amount sent from the source account."""

    source_currency: str = FieldInfo(alias="sourceCurrency")
    """The currency of the source amount."""

    status: Literal["in_progress", "held_for_review", "completed", "failed", "cancelled"]
    """Current processing status of the payment."""

    target_amount: Optional[float] = FieldInfo(alias="targetAmount", default=None)
    """The amount received by the beneficiary in target currency."""

    target_currency: str = FieldInfo(alias="targetCurrency")
    """The currency the beneficiary will receive."""

    estimated_completion_time: Optional[datetime] = FieldInfo(alias="estimatedCompletionTime", default=None)
    """Estimated date and time when the payment will be completed."""

    message: Optional[str] = None
    """Additional messages, e.g., if payment is held for review."""

    tracking_url: Optional[str] = FieldInfo(alias="trackingUrl", default=None)
    """URL to a tracking page for the payment."""
