# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .address import Address
from .._models import BaseModel

__all__ = ["Transaction", "Location", "MerchantDetails"]


class Location(BaseModel):
    city: Optional[str] = None
    """City where the transaction occurred."""

    latitude: Optional[float] = None
    """Latitude coordinate of the transaction."""

    longitude: Optional[float] = None
    """Longitude coordinate of the transaction."""

    state: Optional[str] = None
    """State where the transaction occurred."""

    zip: Optional[str] = None
    """Zip code where the transaction occurred."""


class MerchantDetails(BaseModel):
    address: Optional[Address] = None
    """Physical address of the merchant."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL to the merchant's logo."""

    name: Optional[str] = None
    """Official name of the merchant."""

    phone: Optional[str] = None
    """Merchant's phone number."""

    website: Optional[str] = None
    """Merchant's website URL."""


class Transaction(BaseModel):
    id: str
    """Unique identifier for the transaction."""

    account_id: str = FieldInfo(alias="accountId")
    """ID of the account from which the transaction occurred."""

    amount: float
    """Amount of the transaction."""

    category: str
    """
    AI-assigned or user-defined category of the transaction (e.g., 'Groceries',
    'Utilities').
    """

    currency: str
    """ISO 4217 currency code of the transaction."""

    date: datetime.date
    """Date the transaction occurred (local date)."""

    description: str
    """Detailed description of the transaction."""

    type: Literal["income", "expense", "transfer", "investment", "refund", "bill_payment"]
    """Type of the transaction."""

    ai_category_confidence: Optional[float] = FieldInfo(alias="aiCategoryConfidence", default=None)
    """AI confidence score for the assigned category (0-1)."""

    carbon_footprint: Optional[float] = FieldInfo(alias="carbonFootprint", default=None)
    """Estimated carbon footprint in kg CO2e for this transaction, derived by AI."""

    dispute_status: Optional[Literal["none", "pending", "under_review", "resolved", "rejected"]] = FieldInfo(
        alias="disputeStatus", default=None
    )
    """Current dispute status of the transaction."""

    location: Optional[Location] = None
    """Geographic location details for a transaction."""

    merchant_details: Optional[MerchantDetails] = FieldInfo(alias="merchantDetails", default=None)
    """Detailed information about a merchant associated with a transaction."""

    notes: Optional[str] = None
    """Personal notes added by the user to the transaction."""

    payment_channel: Optional[Literal["in_store", "online", "mobile", "ATM", "bill_payment", "transfer", "other"]] = (
        FieldInfo(alias="paymentChannel", default=None)
    )
    """Channel through which the payment was made."""

    posted_date: Optional[datetime.date] = FieldInfo(alias="postedDate", default=None)
    """Date the transaction was posted to the account (local date)."""

    receipt_url: Optional[str] = FieldInfo(alias="receiptUrl", default=None)
    """URL to a digital receipt for the transaction."""

    tags: Optional[List[str]] = None
    """User-defined tags for the transaction."""
