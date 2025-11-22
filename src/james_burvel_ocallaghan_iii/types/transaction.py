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
    """City name."""

    country: Optional[str] = None
    """Country code (ISO 3166-1 alpha-2)."""

    latitude: Optional[float] = None
    """Latitude coordinate."""

    longitude: Optional[float] = None
    """Longitude coordinate."""

    state: Optional[str] = None
    """State or province code."""


class MerchantDetails(BaseModel):
    address: Optional[Address] = None
    """Physical address of the merchant."""

    category: Optional[str] = None
    """Standardized industry category for the merchant."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL to the merchant's logo."""

    name: Optional[str] = None
    """Name of the merchant."""

    website: Optional[str] = None
    """Merchant's website URL."""


class Transaction(BaseModel):
    id: str
    """Unique identifier for the transaction."""

    account_id: str = FieldInfo(alias="accountId")
    """The ID of the account this transaction belongs to."""

    amount: float
    """Amount of the transaction.

    Positive for income/refunds, negative for expenses/transfers out.
    """

    category: str
    """
    AI-assigned or user-defined category of the transaction (e.g., 'Groceries',
    'Utilities').
    """

    currency: str
    """The currency of the transaction (ISO 4217 code)."""

    date: datetime.date
    """The date the transaction occurred."""

    description: str
    """Detailed description of the transaction as it appears on the statement."""

    type: Literal["income", "expense", "transfer", "investment", "refund", "bill_payment"]
    """Type of transaction."""

    ai_category_confidence: Optional[float] = FieldInfo(alias="aiCategoryConfidence", default=None)
    """AI's confidence score (0-1) in its category assignment."""

    carbon_footprint: Optional[float] = FieldInfo(alias="carbonFootprint", default=None)
    """
    Estimated carbon footprint (in Kg CO2e) associated with the transaction, if
    available.
    """

    dispute_status: Optional[Literal["none", "pending", "under_review", "resolved", "rejected"]] = FieldInfo(
        alias="disputeStatus", default=None
    )
    """Current status of any dispute initiated for this transaction."""

    location: Optional[Location] = None
    """Geographic location where the transaction occurred."""

    merchant_details: Optional[MerchantDetails] = FieldInfo(alias="merchantDetails", default=None)
    """Details about the merchant involved in the transaction."""

    notes: Optional[str] = None
    """Personal notes added by the user to the transaction."""

    payment_channel: Optional[
        Literal["in_store", "online", "atm", "transfer", "bill_payment", "recurring", "other"]
    ] = FieldInfo(alias="paymentChannel", default=None)
    """The channel through which the payment was made."""

    posted_date: Optional[datetime.date] = FieldInfo(alias="postedDate", default=None)
    """The date the transaction was posted to the account (may differ from `date`)."""

    receipt_url: Optional[str] = FieldInfo(alias="receiptUrl", default=None)
    """URL to a digital receipt for the transaction."""

    tags: Optional[List[str]] = None
    """User-defined tags for the transaction."""
