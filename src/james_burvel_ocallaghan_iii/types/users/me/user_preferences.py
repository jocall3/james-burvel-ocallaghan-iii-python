# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserPreferences", "NotificationChannels"]


class NotificationChannels(BaseModel):
    email: Optional[bool] = None
    """Receive notifications via email."""

    in_app: Optional[bool] = FieldInfo(alias="inApp", default=None)
    """Receive notifications within the application."""

    push: Optional[bool] = None
    """Receive push notifications to connected devices."""

    sms: Optional[bool] = None
    """Receive notifications via SMS."""


class UserPreferences(BaseModel):
    ai_interaction_mode: Optional[Literal["passive", "balanced", "proactive"]] = FieldInfo(
        alias="aiInteractionMode", default=None
    )
    """How actively the AI should provide advice and suggestions."""

    data_sharing_consent: Optional[bool] = FieldInfo(alias="dataSharingConsent", default=None)
    """Consent for sharing anonymized data for AI improvements."""

    notification_channels: Optional[NotificationChannels] = FieldInfo(alias="notificationChannels", default=None)
    """Enabled notification channels."""

    preferred_language: Optional[str] = FieldInfo(alias="preferredLanguage", default=None)
    """User's preferred language for the interface."""

    theme: Optional[Literal["Light-Default", "Dark-Quantum", "Eco-Green", "Minimalist"]] = None
    """User's selected UI theme."""

    transaction_grouping: Optional[Literal["category", "merchant", "date", "account"]] = FieldInfo(
        alias="transactionGrouping", default=None
    )
    """Default grouping preference for transaction lists."""
