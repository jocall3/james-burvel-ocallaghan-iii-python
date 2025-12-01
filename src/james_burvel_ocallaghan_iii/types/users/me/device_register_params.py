# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeviceRegisterParams"]


class DeviceRegisterParams(TypedDict, total=False):
    device_type: Required[
        Annotated[Literal["mobile", "desktop", "tablet", "smart_watch"], PropertyInfo(alias="deviceType")]
    ]
    """Type of the device being registered."""

    model: Required[object]
    """Model of the device."""

    os: Required[object]
    """Operating system of the device."""

    biometric_signature: Annotated[object, PropertyInfo(alias="biometricSignature")]
    """
    Optional: Base64 encoded biometric signature for initial enrollment (e.g., for
    Passkey registration).
    """

    device_name: Annotated[object, PropertyInfo(alias="deviceName")]
    """Optional: A friendly name for the device."""

    push_token: Annotated[object, PropertyInfo(alias="pushToken")]
    """Optional: Push notification token for the device."""
