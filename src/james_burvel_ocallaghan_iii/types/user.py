# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .address import Address
from .._models import BaseModel
from .users.me.user_preferences import UserPreferences

__all__ = ["User", "SecurityStatus"]


class SecurityStatus(BaseModel):
    biometrics_enrolled: Optional[object] = FieldInfo(alias="biometricsEnrolled", default=None)
    """Indicates if biometric authentication is enrolled."""

    last_login: Optional[object] = FieldInfo(alias="lastLogin", default=None)
    """Timestamp of the last successful login."""

    last_login_ip: Optional[object] = FieldInfo(alias="lastLoginIp", default=None)
    """IP address of the last successful login."""

    two_factor_enabled: Optional[object] = FieldInfo(alias="twoFactorEnabled", default=None)
    """Indicates if two-factor authentication (2FA) is enabled."""


class User(BaseModel):
    id: object
    """Unique identifier for the user."""

    email: object
    """Primary email address of the user."""

    identity_verified: object = FieldInfo(alias="identityVerified")
    """Indicates if the user's identity has been verified (e.g., via KYC)."""

    name: object
    """Full name of the user."""

    address: Optional[Address] = None

    ai_persona: Optional[object] = FieldInfo(alias="aiPersona", default=None)
    """AI-identified financial persona for tailored advice."""

    date_of_birth: Optional[object] = FieldInfo(alias="dateOfBirth", default=None)
    """Date of birth of the user (YYYY-MM-DD)."""

    gamification_level: Optional[object] = FieldInfo(alias="gamificationLevel", default=None)
    """Current gamification level."""

    loyalty_points: Optional[object] = FieldInfo(alias="loyaltyPoints", default=None)
    """Current balance of loyalty points."""

    loyalty_tier: Optional[object] = FieldInfo(alias="loyaltyTier", default=None)
    """Current loyalty program tier."""

    phone: Optional[object] = None
    """Primary phone number of the user."""

    preferences: Optional[UserPreferences] = None
    """User's personalized preferences for the platform."""

    security_status: Optional[SecurityStatus] = FieldInfo(alias="securityStatus", default=None)
    """Security-related status for the user account."""
