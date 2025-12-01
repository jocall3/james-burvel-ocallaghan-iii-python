# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BiometricEnrollParams"]


class BiometricEnrollParams(TypedDict, total=False):
    biometric_signature: Required[Annotated[object, PropertyInfo(alias="biometricSignature")]]
    """Base64 encoded representation of the biometric template or proof."""

    biometric_type: Required[
        Annotated[
            Literal["fingerprint", "facial_recognition", "voice_recognition"], PropertyInfo(alias="biometricType")
        ]
    ]
    """The type of biometric data being enrolled."""

    device_id: Required[Annotated[object, PropertyInfo(alias="deviceId")]]
    """The ID of the device on which the biometric is being enrolled."""

    device_name: Annotated[object, PropertyInfo(alias="deviceName")]
    """Optional: A friendly name for the device, if not already linked."""
