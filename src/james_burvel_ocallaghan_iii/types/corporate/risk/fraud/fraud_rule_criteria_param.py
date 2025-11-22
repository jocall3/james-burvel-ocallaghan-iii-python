# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["FraudRuleCriteriaParam"]


class FraudRuleCriteriaParam(TypedDict, total=False):
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
