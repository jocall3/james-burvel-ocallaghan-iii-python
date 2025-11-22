# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["RuleUpdateParams", "Action", "Criteria"]


class RuleUpdateParams(TypedDict, total=False):
    action: Action
    """Updated action to take when the rule is triggered."""

    criteria: Criteria
    """Updated criteria for the rule."""

    description: str
    """Updated description of what the rule detects."""

    name: str
    """Updated name of the fraud rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Updated severity level."""

    status: Literal["active", "inactive", "draft"]
    """Updated status of the rule."""


class Action(TypedDict, total=False):
    details: Required[str]
    """Details or instructions for the action."""

    type: Required[Literal["block", "alert", "auto_review", "manual_review", "request_mfa"]]
    """Type of action to perform."""

    target_team: Annotated[Optional[str], PropertyInfo(alias="targetTeam")]
    """The team or department to notify for alerts/reviews."""


class Criteria(TypedDict, total=False):
    account_inactivity_days: Annotated[Optional[int], PropertyInfo(alias="accountInactivityDays")]
    """Number of days an account must be inactive for the rule to apply."""

    country_of_origin: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="countryOfOrigin")]
    """List of ISO 2-letter country codes for transaction origin."""

    geographic_distance_km: Annotated[Optional[int], PropertyInfo(alias="geographicDistanceKm")]
    """Minimum geographic distance (in km) from recent activity for anomaly."""

    last_login_days: Annotated[Optional[int], PropertyInfo(alias="lastLoginDays")]
    """Number of days since last user login for anomaly detection."""

    no_travel_notification: Annotated[Optional[bool], PropertyInfo(alias="noTravelNotification")]
    """If true, rule applies only if no prior travel notification was made."""

    payment_count_min: Annotated[Optional[int], PropertyInfo(alias="paymentCountMin")]
    """Minimum number of payments in a timeframe."""

    recipient_country_risk_level: Annotated[
        Optional[List[Literal["Low", "Medium", "High", "Very High"]]], PropertyInfo(alias="recipientCountryRiskLevel")
    ]
    """List of risk levels for recipient countries."""

    recipient_new: Annotated[Optional[bool], PropertyInfo(alias="recipientNew")]
    """If true, recipient must be a new payee."""

    timeframe_hours: Annotated[Optional[int], PropertyInfo(alias="timeframeHours")]
    """Timeframe in hours for payment count or other event aggregations."""

    transaction_amount_min: Annotated[Optional[float], PropertyInfo(alias="transactionAmountMin")]
    """Minimum transaction amount to consider."""

    transaction_type: Annotated[Optional[Literal["debit", "credit"]], PropertyInfo(alias="transactionType")]
    """Specific transaction type (e.g., debit, credit)."""
