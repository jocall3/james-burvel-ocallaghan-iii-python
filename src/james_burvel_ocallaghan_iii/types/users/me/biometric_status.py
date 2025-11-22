# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BiometricStatus", "EnrolledBiometric"]


class EnrolledBiometric(BaseModel):
    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)

    enrollment_date: Optional[datetime] = FieldInfo(alias="enrollmentDate", default=None)

    type: Optional[Literal["fingerprint", "facial_recognition", "voice_recognition"]] = None


class BiometricStatus(BaseModel):
    biometrics_enrolled: bool = FieldInfo(alias="biometricsEnrolled")
    """Overall status indicating if any biometrics are enrolled."""

    enrolled_biometrics: List[EnrolledBiometric] = FieldInfo(alias="enrolledBiometrics")
    """List of specific biometric types and devices enrolled."""

    last_used: Optional[datetime] = FieldInfo(alias="lastUsed", default=None)
    """Timestamp of the last successful biometric authentication."""
