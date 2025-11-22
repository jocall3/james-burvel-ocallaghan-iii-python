# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from pydantic import Field as FieldInfo

from .address import Address
from .._models import BaseModel
from .users.me.user_preferences import UserPreferences

__all__ = ["User", "SecurityStatus"]


class SecurityStatus(BaseModel):
    biometrics_enrolled: Optional[bool] = FieldInfo(alias="biometricsEnrolled", default=None)
    """Indicates if biometric authentication is enrolled."""

    last_login: Optional[datetime] = FieldInfo(alias="lastLogin", default=None)
    """Timestamp of the last successful login."""

    last_login_ip: Optional[str] = FieldInfo(alias="lastLoginIp", default=None)
    """IP address of the last successful login."""

    two_factor_enabled: Optional[bool] = FieldInfo(alias="twoFactorEnabled", default=None)
    """Indicates if two-factor authentication (2FA) is enabled."""


class User(BaseModel):
    id: str
    """Unique identifier for the user."""

    email: str
    """Primary email address of the user."""

    identity_verified: bool = FieldInfo(alias="identityVerified")
    """Indicates if the user's identity has been verified (e.g., via KYC)."""

    name: str
    """Full name of the user."""

    address: Optional[Address] = None

    ai_persona: Optional[str] = FieldInfo(alias="aiPersona", default=None)
    """AI-identified financial persona for tailored advice."""

    date_of_birth: Optional[date] = FieldInfo(alias="dateOfBirth", default=None)
    """Date of birth of the user (YYYY-MM-DD)."""

    gamification_level: Optional[int] = FieldInfo(alias="gamificationLevel", default=None)
    """Current gamification level."""

    loyalty_points: Optional[int] = FieldInfo(alias="loyaltyPoints", default=None)
    """Current balance of loyalty points."""

    loyalty_tier: Optional[str] = FieldInfo(alias="loyaltyTier", default=None)
    """Current loyalty program tier."""

    phone: Optional[str] = None
    """Primary phone number of the user."""

    preferences: Optional[UserPreferences] = None
    """User's personalized preferences for the platform."""

    security_status: Optional[SecurityStatus] = FieldInfo(alias="securityStatus", default=None)
    """Security-related status for the user account."""
