# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeviceRegisterParams"]


class DeviceRegisterParams(TypedDict, total=False):
    device_type: Required[
        Annotated[Literal["mobile", "desktop", "tablet", "smart_watch"], PropertyInfo(alias="deviceType")]
    ]
    """Type of device being registered."""

    model: Required[str]
    """Model of the device."""

    os: Required[str]
    """Operating system and version of the device."""

    biometric_signature: Annotated[Optional[str], PropertyInfo(alias="biometricSignature")]
    """Base64 encoded biometric signature for initial enrollment (if applicable)."""

    device_name: Annotated[Optional[str], PropertyInfo(alias="deviceName")]
    """User-defined name for the device."""

    push_token: Annotated[Optional[str], PropertyInfo(alias="pushToken")]
    """Push notification token for the device."""
