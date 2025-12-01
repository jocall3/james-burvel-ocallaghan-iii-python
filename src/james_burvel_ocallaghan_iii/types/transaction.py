# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .address import Address
from .._models import BaseModel

__all__ = ["Transaction", "Location", "MerchantDetails"]


class Location(BaseModel):
    city: Optional[object] = None
    """City where the transaction occurred."""

    latitude: Optional[object] = None
    """Latitude coordinate of the transaction."""

    longitude: Optional[object] = None
    """Longitude coordinate of the transaction."""

    state: Optional[object] = None
    """State where the transaction occurred."""

    zip: Optional[object] = None
    """Zip code where the transaction occurred."""


class MerchantDetails(BaseModel):
    address: Optional[Address] = None

    logo_url: Optional[object] = FieldInfo(alias="logoUrl", default=None)
    """URL to the merchant's logo."""

    name: Optional[object] = None
    """Official name of the merchant."""

    phone: Optional[object] = None
    """Merchant's phone number."""

    website: Optional[object] = None
    """Merchant's website URL."""


class Transaction(BaseModel):
    id: object
    """Unique identifier for the transaction."""

    account_id: object = FieldInfo(alias="accountId")
    """ID of the account from which the transaction occurred."""

    amount: object
    """Amount of the transaction."""

    category: object
    """
    AI-assigned or user-defined category of the transaction (e.g., 'Groceries',
    'Utilities').
    """

    currency: object
    """ISO 4217 currency code of the transaction."""

    date: object
    """Date the transaction occurred (local date)."""

    description: object
    """Detailed description of the transaction."""

    type: Literal["income", "expense", "transfer", "investment", "refund", "bill_payment"]
    """Type of the transaction."""

    ai_category_confidence: Optional[object] = FieldInfo(alias="aiCategoryConfidence", default=None)
    """AI confidence score for the assigned category (0-1)."""

    carbon_footprint: Optional[object] = FieldInfo(alias="carbonFootprint", default=None)
    """Estimated carbon footprint in kg CO2e for this transaction, derived by AI."""

    dispute_status: Optional[Literal["none", "pending", "under_review", "resolved", "rejected"]] = FieldInfo(
        alias="disputeStatus", default=None
    )
    """Current dispute status of the transaction."""

    location: Optional[Location] = None
    """Geographic location details for a transaction."""

    merchant_details: Optional[MerchantDetails] = FieldInfo(alias="merchantDetails", default=None)
    """Detailed information about a merchant associated with a transaction."""

    notes: Optional[object] = None
    """Personal notes added by the user to the transaction."""

    payment_channel: Optional[Literal["in_store", "online", "mobile", "ATM", "bill_payment", "transfer", "other"]] = (
        FieldInfo(alias="paymentChannel", default=None)
    )
    """Channel through which the payment was made."""

    posted_date: Optional[object] = FieldInfo(alias="postedDate", default=None)
    """Date the transaction was posted to the account (local date)."""

    receipt_url: Optional[object] = FieldInfo(alias="receiptUrl", default=None)
    """URL to a digital receipt for the transaction."""

    tags: Optional[List[object]] = None
    """User-defined tags for the transaction."""
