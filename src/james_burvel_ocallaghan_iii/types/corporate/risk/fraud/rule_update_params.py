# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["RuleUpdateParams", "Action", "Criteria"]


class RuleUpdateParams(TypedDict, total=False):
    action: Action
    """Updated automated action to take when this rule is triggered.

    All fields are optional for partial updates.
    """

    ai_learning_enabled: Annotated[bool, PropertyInfo(alias="aiLearningEnabled")]
    """Update AI learning status for this rule."""

    criteria: Criteria
    """Updated conditions that trigger this fraud rule.

    All fields are optional for partial updates.
    """

    description: str
    """Updated description of what the rule detects."""

    name: str
    """Updated name of the fraud rule."""

    priority: int
    """Updated processing priority of the rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Updated default severity assigned to anomalies."""

    status: Literal["active", "inactive", "draft"]
    """Updated status of the rule."""


class Action(TypedDict, total=False):
    details: Required[str]
    """Detailed description of the action."""

    type: Required[Literal["flag", "alert", "block", "auto_review", "mfa_challenge"]]
    """The type of action to take (e.g., flag for review, block transaction)."""

    target_channels: Annotated[
        Optional[List[Literal["email", "sms", "push", "in_app", "dashboard", "api_webhook"]]],
        PropertyInfo(alias="targetChannels"),
    ]
    """Channels to send alerts/notifications to."""


class Criteria(TypedDict, total=False):
    account_inactivity_days: Annotated[Optional[int], PropertyInfo(alias="accountInactivityDays")]
    """Number of days an account must be inactive to trigger the rule."""

    country_of_origin: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="countryOfOrigin")]
    """Transaction origin countries to match (ISO 3166-1 alpha-2)."""

    geographic_distance_km: Annotated[Optional[int], PropertyInfo(alias="geographicDistanceKm")]
    """Minimum geographic distance from user's usual activity to trigger."""

    keywords_in_description: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="keywordsInDescription")]
    """Keywords or phrases in transaction description to flag."""

    last_login_days: Annotated[Optional[int], PropertyInfo(alias="lastLoginDays")]
    """If transaction is far from last login within this many days."""

    no_travel_notification: Annotated[Optional[bool], PropertyInfo(alias="noTravelNotification")]
    """True if no travel notification was filed for geographic mismatch."""

    payment_count_min: Annotated[Optional[int], PropertyInfo(alias="paymentCountMin")]
    """Minimum number of payments within a timeframe to trigger."""

    recipient_country_risk_level: Annotated[
        Optional[List[Literal["Low", "Medium", "High", "Very High"]]], PropertyInfo(alias="recipientCountryRiskLevel")
    ]
    """Recipient countries by risk level to match."""

    recipient_new: Annotated[Optional[bool], PropertyInfo(alias="recipientNew")]
    """True if the recipient is a new beneficiary."""

    timeframe_hours: Annotated[Optional[int], PropertyInfo(alias="timeframeHours")]
    """Timeframe in hours for payment count criteria."""

    transaction_amount_max: Annotated[Optional[float], PropertyInfo(alias="transactionAmountMax")]
    """Maximum transaction amount to trigger the rule."""

    transaction_amount_min: Annotated[Optional[float], PropertyInfo(alias="transactionAmountMin")]
    """Minimum transaction amount to trigger the rule."""

    transaction_type: Annotated[Optional[Literal["debit", "credit", "all"]], PropertyInfo(alias="transactionType")]
    """Type of transaction to monitor."""
