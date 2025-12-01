# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Device"]


class Device(BaseModel):
    id: object
    """Unique identifier for the device."""

    ip_address: object = FieldInfo(alias="ipAddress")
    """Last known IP address of the device."""

    last_active: object = FieldInfo(alias="lastActive")
    """Timestamp of the last activity from this device."""

    model: object
    """Model of the device."""

    os: object
    """Operating system of the device."""

    trust_level: Literal["trusted", "pending_verification", "untrusted", "blocked"] = FieldInfo(alias="trustLevel")
    """Security trust level of the device."""

    type: Literal["mobile", "desktop", "tablet", "smart_watch"]
    """Type of the device."""

    device_name: Optional[object] = FieldInfo(alias="deviceName", default=None)
    """User-assigned name for the device."""

    push_token: Optional[object] = FieldInfo(alias="pushToken", default=None)
    """Push notification token for the device."""
