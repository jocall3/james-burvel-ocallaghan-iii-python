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
    """City name of the transaction location."""

    country: Optional[str] = None
    """Country of the transaction location."""

    latitude: Optional[float] = None
    """Latitude coordinate."""

    longitude: Optional[float] = None
    """Longitude coordinate."""

    state: Optional[str] = None
    """State or province of the transaction location."""


class MerchantDetails(BaseModel):
    address: Optional[Address] = None
    """Merchant's physical address."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL to the merchant's logo."""

    name: Optional[str] = None
    """Name of the merchant."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Merchant's phone number."""

    website: Optional[str] = None
    """Merchant's website URL."""


class Transaction(BaseModel):
    id: str
    """Unique identifier for the transaction."""

    account_id: str = FieldInfo(alias="accountId")
    """The ID of the account this transaction belongs to."""

    amount: float
    """The transaction amount."""

    category: str
    """
    AI-assigned or user-defined category of the transaction (e.g., Groceries, Rent,
    Salary).
    """

    currency: str
    """ISO 4217 currency code of the transaction."""

    date: datetime.date
    """The date the transaction occurred (transaction date)."""

    description: str
    """Detailed description of the transaction."""

    type: Literal["income", "expense", "transfer", "investment", "refund", "bill_payment"]
    """Type of the transaction."""

    ai_category_confidence: Optional[float] = FieldInfo(alias="aiCategoryConfidence", default=None)
    """AI's confidence score (0-1) for its category assignment."""

    carbon_footprint: Optional[float] = FieldInfo(alias="carbonFootprint", default=None)
    """Estimated carbon footprint (in Kg CO2e) associated with the transaction."""

    dispute_status: Optional[
        Literal["none", "pending", "under_review", "resolved_in_favor_user", "resolved_in_favor_merchant", "rejected"]
    ] = FieldInfo(alias="disputeStatus", default=None)
    """Current status of any dispute related to this transaction."""

    location: Optional[Location] = None
    """Geolocation details of the transaction, if available."""

    merchant_details: Optional[MerchantDetails] = FieldInfo(alias="merchantDetails", default=None)
    """Detailed information about the merchant."""

    notes: Optional[str] = None
    """Personal notes added by the user to the transaction."""

    payment_channel: Optional[Literal["in_store", "online", "atm", "transfer", "bill_payment", "subscription"]] = (
        FieldInfo(alias="paymentChannel", default=None)
    )
    """Channel through which the payment was made."""

    posted_date: Optional[datetime.date] = FieldInfo(alias="postedDate", default=None)
    """The date the transaction was posted to the account (cleared date)."""

    receipt_url: Optional[str] = FieldInfo(alias="receiptUrl", default=None)
    """URL to a digital receipt for the transaction."""

    tags: Optional[List[str]] = None
    """User-defined tags for the transaction."""
