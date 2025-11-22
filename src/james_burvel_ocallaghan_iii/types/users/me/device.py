# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Device"]


class Device(BaseModel):
    id: str
    """Unique identifier for the device."""

    ip_address: str = FieldInfo(alias="ipAddress")
    """Last known IP address of the device."""

    last_active: datetime = FieldInfo(alias="lastActive")
    """Timestamp of last activity from this device."""

    model: str
    """Device model."""

    os: str
    """Operating system and version."""

    trust_level: Literal["trusted", "untrusted", "pending_verification"] = FieldInfo(alias="trustLevel")
    """Security trust level of the device."""

    type: Literal["mobile", "desktop", "tablet", "smart_watch"]
    """Type of device."""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """User-defined name for the device."""

    push_token: Optional[str] = FieldInfo(alias="pushToken", default=None)
    """Push notification token for the device."""
