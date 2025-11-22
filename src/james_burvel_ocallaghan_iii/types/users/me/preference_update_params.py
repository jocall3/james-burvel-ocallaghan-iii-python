# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PreferenceUpdateParams", "NotificationChannels"]


class PreferenceUpdateParams(TypedDict, total=False):
    ai_interaction_mode: Annotated[Literal["passive", "balanced", "proactive"], PropertyInfo(alias="aiInteractionMode")]
    """How actively the AI should provide advice and suggestions."""

    data_sharing_consent: Annotated[bool, PropertyInfo(alias="dataSharingConsent")]
    """Consent for sharing anonymized data for AI improvements."""

    notification_channels: Annotated[NotificationChannels, PropertyInfo(alias="notificationChannels")]
    """Enabled notification channels."""

    preferred_language: Annotated[str, PropertyInfo(alias="preferredLanguage")]
    """User's preferred language for the interface."""

    theme: Literal["Light-Default", "Dark-Quantum", "Eco-Green", "Minimalist"]
    """User's selected UI theme."""

    transaction_grouping: Annotated[
        Literal["category", "merchant", "date", "account"], PropertyInfo(alias="transactionGrouping")
    ]
    """Default grouping preference for transaction lists."""


class NotificationChannels(TypedDict, total=False):
    email: bool
    """Receive notifications via email."""

    in_app: Annotated[bool, PropertyInfo(alias="inApp")]
    """Receive notifications within the application."""

    push: bool
    """Receive push notifications to connected devices."""

    sms: bool
    """Receive notifications via SMS."""
