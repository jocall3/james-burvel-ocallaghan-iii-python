# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .user_preferences_notification_channels import UserPreferencesNotificationChannels

__all__ = ["UserPreferences"]


class UserPreferences(BaseModel):
    """User's personalized preferences for the platform."""

    ai_interaction_mode: Optional[Literal["proactive", "balanced", "on_demand"]] = FieldInfo(
        alias="aiInteractionMode", default=None
    )
    """
    How the user prefers to interact with AI (proactive advice, balanced, or only on
    demand).
    """

    data_sharing_consent: Optional[object] = FieldInfo(alias="dataSharingConsent", default=None)
    """
    Consent status for sharing anonymized data for AI improvement and personalized
    offers.
    """

    notification_channels: Optional[UserPreferencesNotificationChannels] = FieldInfo(
        alias="notificationChannels", default=None
    )
    """Preferred channels for receiving notifications."""

    preferred_language: Optional[object] = FieldInfo(alias="preferredLanguage", default=None)
    """Preferred language for the user interface."""

    theme: Optional[object] = None
    """Preferred UI theme (e.g., Light-Default, Dark-Quantum)."""

    transaction_grouping: Optional[Literal["category", "merchant", "date", "account"]] = FieldInfo(
        alias="transactionGrouping", default=None
    )
    """Default grouping preference for transaction lists."""
