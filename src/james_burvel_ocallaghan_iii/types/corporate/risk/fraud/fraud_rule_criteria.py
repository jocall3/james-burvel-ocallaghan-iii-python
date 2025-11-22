# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FraudRuleCriteria"]


class FraudRuleCriteria(BaseModel):
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
