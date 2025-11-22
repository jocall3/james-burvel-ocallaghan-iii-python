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
    """City name of the location."""

    country: Optional[str] = None
    """Country of the location."""

    latitude: Optional[float] = None
    """Latitude coordinate."""

    longitude: Optional[float] = None
    """Longitude coordinate."""

    state: Optional[str] = None
    """State or province of the location."""


class MerchantDetails(BaseModel):
    address: Optional[Address] = None
    """Physical address of the merchant."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL to the merchant's logo."""

    name: Optional[str] = None
    """Full name of the merchant."""

    website: Optional[str] = None
    """Merchant's website URL."""


class Transaction(BaseModel):
    id: str
    """Unique identifier for the transaction."""

    account_id: str = FieldInfo(alias="accountId")
    """The ID of the account the transaction belongs to."""

    amount: float
    """The amount of the transaction."""

    category: str
    """AI-assigned or user-defined category for the transaction."""

    currency: str
    """The currency of the transaction (ISO 4217 code)."""

    date: datetime.date
    """The date the transaction occurred (transaction date)."""

    description: str
    """Detailed description of the transaction (merchant name, etc.)."""

    dispute_status: Literal[
        "none", "pending", "under_review", "resolved_in_favor_user", "resolved_in_favor_merchant", "rejected"
    ] = FieldInfo(alias="disputeStatus")
    """Current status of any dispute related to this transaction."""

    type: Literal["income", "expense", "transfer", "investment", "refund", "bill_payment", "fee"]
    """Type of the transaction (e.g., income, expense)."""

    ai_category_confidence: Optional[float] = FieldInfo(alias="aiCategoryConfidence", default=None)
    """AI's confidence score (0-1) for its category assignment."""

    carbon_footprint: Optional[float] = FieldInfo(alias="carbonFootprint", default=None)
    """Estimated carbon footprint (in Kg CO2e) associated with the transaction."""

    location: Optional[Location] = None
    """Geographic location where the transaction took place."""

    merchant_details: Optional[MerchantDetails] = FieldInfo(alias="merchantDetails", default=None)
    """Detailed information about the merchant involved in the transaction."""

    notes: Optional[str] = None
    """User-added personal notes for the transaction."""

    payment_channel: Optional[Literal["in_store", "online", "atm", "transfer", "bill_payment", "recurring"]] = (
        FieldInfo(alias="paymentChannel", default=None)
    )
    """The channel through which the payment was made."""

    posted_date: Optional[datetime.date] = FieldInfo(alias="postedDate", default=None)
    """The date the transaction was posted to the account (cleared date)."""

    receipt_url: Optional[str] = FieldInfo(alias="receiptUrl", default=None)
    """URL to a digital receipt if available."""

    tags: Optional[List[str]] = None
    """User-defined tags for the transaction."""
