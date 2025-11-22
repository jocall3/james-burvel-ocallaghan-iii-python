# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserPreferencesParam", "NotificationChannels"]


class NotificationChannels(TypedDict, total=False):
    email: bool

    in_app: Annotated[bool, PropertyInfo(alias="inApp")]

    push: bool

    sms: bool


class UserPreferencesParam(TypedDict, total=False):
    ai_interaction_mode: Annotated[
        Literal["proactive", "balanced", "on_demand"], PropertyInfo(alias="aiInteractionMode")
    ]
    """
    How the user prefers to interact with AI (proactive advice, balanced, or only on
    demand).
    """

    data_sharing_consent: Annotated[bool, PropertyInfo(alias="dataSharingConsent")]
    """
    Consent status for sharing anonymized data for AI improvement and personalized
    offers.
    """

    notification_channels: Annotated[NotificationChannels, PropertyInfo(alias="notificationChannels")]
    """Preferred channels for receiving notifications."""

    preferred_language: Annotated[str, PropertyInfo(alias="preferredLanguage")]
    """Preferred language for the user interface."""

    theme: str
    """Preferred UI theme (e.g., Light-Default, Dark-Quantum)."""

    transaction_grouping: Annotated[
        Literal["category", "merchant", "date", "account"], PropertyInfo(alias="transactionGrouping")
    ]
    """Default grouping preference for transaction lists."""
