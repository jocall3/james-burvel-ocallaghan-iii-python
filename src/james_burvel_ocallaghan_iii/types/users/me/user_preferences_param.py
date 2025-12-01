# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo
from .user_preferences_notification_channels_param import UserPreferencesNotificationChannelsParam

__all__ = ["UserPreferencesParam"]


class UserPreferencesParam(TypedDict, total=False):
    ai_interaction_mode: Annotated[
        Literal["proactive", "balanced", "on_demand"], PropertyInfo(alias="aiInteractionMode")
    ]
    """
    How the user prefers to interact with AI (proactive advice, balanced, or only on
    demand).
    """

    data_sharing_consent: Annotated[object, PropertyInfo(alias="dataSharingConsent")]
    """
    Consent status for sharing anonymized data for AI improvement and personalized
    offers.
    """

    notification_channels: Annotated[
        UserPreferencesNotificationChannelsParam, PropertyInfo(alias="notificationChannels")
    ]
    """Preferred channels for receiving notifications."""

    preferred_language: Annotated[object, PropertyInfo(alias="preferredLanguage")]
    """Preferred language for the user interface."""

    theme: object
    """Preferred UI theme (e.g., Light-Default, Dark-Quantum)."""

    transaction_grouping: Annotated[
        Literal["category", "merchant", "date", "account"], PropertyInfo(alias="transactionGrouping")
    ]
    """Default grouping preference for transaction lists."""
