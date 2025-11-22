# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FraudRule", "Action", "Criteria"]


class Action(BaseModel):
    details: str
    """Details or instructions for the action."""

    type: Literal["block", "alert", "auto_review", "manual_review", "request_mfa"]
    """Type of action to perform."""

    target_team: Optional[str] = FieldInfo(alias="targetTeam", default=None)
    """The team or department to notify for alerts/reviews."""


class Criteria(BaseModel):
    account_inactivity_days: Optional[int] = FieldInfo(alias="accountInactivityDays", default=None)
    """Number of days an account must be inactive for the rule to apply."""

    country_of_origin: Optional[List[str]] = FieldInfo(alias="countryOfOrigin", default=None)
    """List of ISO 2-letter country codes for transaction origin."""

    geographic_distance_km: Optional[int] = FieldInfo(alias="geographicDistanceKm", default=None)
    """Minimum geographic distance (in km) from recent activity for anomaly."""

    last_login_days: Optional[int] = FieldInfo(alias="lastLoginDays", default=None)
    """Number of days since last user login for anomaly detection."""

    no_travel_notification: Optional[bool] = FieldInfo(alias="noTravelNotification", default=None)
    """If true, rule applies only if no prior travel notification was made."""

    payment_count_min: Optional[int] = FieldInfo(alias="paymentCountMin", default=None)
    """Minimum number of payments in a timeframe."""

    recipient_country_risk_level: Optional[List[Literal["Low", "Medium", "High", "Very High"]]] = FieldInfo(
        alias="recipientCountryRiskLevel", default=None
    )
    """List of risk levels for recipient countries."""

    recipient_new: Optional[bool] = FieldInfo(alias="recipientNew", default=None)
    """If true, recipient must be a new payee."""

    timeframe_hours: Optional[int] = FieldInfo(alias="timeframeHours", default=None)
    """Timeframe in hours for payment count or other event aggregations."""

    transaction_amount_min: Optional[float] = FieldInfo(alias="transactionAmountMin", default=None)
    """Minimum transaction amount to consider."""

    transaction_type: Optional[Literal["debit", "credit"]] = FieldInfo(alias="transactionType", default=None)
    """Specific transaction type (e.g., debit, credit)."""


class FraudRule(BaseModel):
    id: str
    """Unique identifier for the fraud detection rule."""

    action: Action
    """Action to take when a fraud rule is triggered."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the rule was created."""

    created_by: str = FieldInfo(alias="createdBy")
    """Identifier of who created the rule (e.g., user ID, 'system:ai-risk-engine')."""

    criteria: Criteria
    """Criteria that define when a fraud rule should trigger."""

    description: str
    """Detailed description of what the rule detects."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the rule was last updated."""

    name: str
    """Name of the fraud rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Severity level when this rule is triggered."""

    status: Literal["active", "inactive", "draft"]
    """Current status of the rule."""
