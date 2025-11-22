# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .address import Address
from .._models import BaseModel
from .users.me.user_preferences import UserPreferences

__all__ = ["User", "SecurityStatus"]


class SecurityStatus(BaseModel):
    biometrics_enrolled: Optional[bool] = FieldInfo(alias="biometricsEnrolled", default=None)
    """Indicates if biometric authentication is enrolled."""

    last_login: Optional[datetime] = FieldInfo(alias="lastLogin", default=None)
    """Timestamp of the user's last successful login."""

    last_login_ip: Optional[str] = FieldInfo(alias="lastLoginIp", default=None)
    """IP address from which the last successful login occurred."""

    two_factor_enabled: Optional[bool] = FieldInfo(alias="twoFactorEnabled", default=None)
    """Indicates if two-factor authentication is enabled."""


class User(BaseModel):
    id: str
    """Unique identifier for the user."""

    email: str
    """Unique email address of the user."""

    name: str
    """Full name of the user."""

    address: Optional[Address] = None
    """User's residential address."""

    ai_persona: Optional[str] = FieldInfo(alias="aiPersona", default=None)
    """AI-assigned financial persona based on user behavior and preferences."""

    date_of_birth: Optional[date] = FieldInfo(alias="dateOfBirth", default=None)
    """User's date of birth."""

    gamification_level: Optional[int] = FieldInfo(alias="gamificationLevel", default=None)
    """Current gamification level of the user."""

    identity_verified: Optional[bool] = FieldInfo(alias="identityVerified", default=None)
    """Indicates if the user's identity has been fully verified (KYC/AML)."""

    loyalty_points: Optional[int] = FieldInfo(alias="loyaltyPoints", default=None)
    """Total loyalty points accumulated by the user."""

    loyalty_tier: Optional[Literal["Bronze", "Silver", "Gold", "Platinum", "Zenith Platinum"]] = FieldInfo(
        alias="loyaltyTier", default=None
    )
    """Current loyalty tier of the user."""

    phone: Optional[str] = None
    """Phone number of the user."""

    preferences: Optional[UserPreferences] = None
    """User's personalization and experience preferences."""

    security_status: Optional[SecurityStatus] = FieldInfo(alias="securityStatus", default=None)
    """Current security status and settings for the user."""
