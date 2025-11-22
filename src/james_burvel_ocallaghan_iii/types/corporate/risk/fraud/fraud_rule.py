# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FraudRule", "Action", "Criteria"]


class Action(BaseModel):
    details: str
    """Detailed description of the action."""

    type: Literal["flag", "alert", "block", "auto_review", "mfa_challenge"]
    """The type of action to take (e.g., flag for review, block transaction)."""

    target_channels: Optional[List[Literal["email", "sms", "push", "in_app", "dashboard", "api_webhook"]]] = FieldInfo(
        alias="targetChannels", default=None
    )
    """Channels to send alerts/notifications to."""


class Criteria(BaseModel):
    account_inactivity_days: Optional[int] = FieldInfo(alias="accountInactivityDays", default=None)
    """Number of days an account must be inactive to trigger the rule."""

    country_of_origin: Optional[List[str]] = FieldInfo(alias="countryOfOrigin", default=None)
    """Transaction origin countries to match (ISO 3166-1 alpha-2)."""

    geographic_distance_km: Optional[int] = FieldInfo(alias="geographicDistanceKm", default=None)
    """Minimum geographic distance from user's usual activity to trigger."""

    keywords_in_description: Optional[List[str]] = FieldInfo(alias="keywordsInDescription", default=None)
    """Keywords or phrases in transaction description to flag."""

    last_login_days: Optional[int] = FieldInfo(alias="lastLoginDays", default=None)
    """If transaction is far from last login within this many days."""

    no_travel_notification: Optional[bool] = FieldInfo(alias="noTravelNotification", default=None)
    """True if no travel notification was filed for geographic mismatch."""

    payment_count_min: Optional[int] = FieldInfo(alias="paymentCountMin", default=None)
    """Minimum number of payments within a timeframe to trigger."""

    recipient_country_risk_level: Optional[List[Literal["Low", "Medium", "High", "Very High"]]] = FieldInfo(
        alias="recipientCountryRiskLevel", default=None
    )
    """Recipient countries by risk level to match."""

    recipient_new: Optional[bool] = FieldInfo(alias="recipientNew", default=None)
    """True if the recipient is a new beneficiary."""

    timeframe_hours: Optional[int] = FieldInfo(alias="timeframeHours", default=None)
    """Timeframe in hours for payment count criteria."""

    transaction_amount_max: Optional[float] = FieldInfo(alias="transactionAmountMax", default=None)
    """Maximum transaction amount to trigger the rule."""

    transaction_amount_min: Optional[float] = FieldInfo(alias="transactionAmountMin", default=None)
    """Minimum transaction amount to trigger the rule."""

    transaction_type: Optional[Literal["debit", "credit", "all"]] = FieldInfo(alias="transactionType", default=None)
    """Type of transaction to monitor."""


class FraudRule(BaseModel):
    id: str
    """Unique identifier for the fraud detection rule."""

    action: Action
    """The automated action to take when this rule is triggered."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the rule was created."""

    created_by: str = FieldInfo(alias="createdBy")
    """Identifier of the user or system that created the rule."""

    criteria: Criteria
    """The conditions that trigger this fraud rule."""

    description: str
    """Detailed description of what the rule detects."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the rule was last updated."""

    name: str
    """Name of the fraud rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """The default severity assigned to anomalies detected by this rule."""

    status: Literal["active", "inactive", "draft"]
    """Current status of the rule."""

    ai_learning_enabled: Optional[bool] = FieldInfo(alias="aiLearningEnabled", default=None)
    """Indicates if AI continuously learns and refines this rule."""

    priority: Optional[int] = None
    """Processing priority of the rule (higher is more urgent)."""
