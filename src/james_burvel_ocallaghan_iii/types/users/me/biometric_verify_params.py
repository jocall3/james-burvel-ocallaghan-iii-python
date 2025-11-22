# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BiometricVerifyParams"]


class BiometricVerifyParams(TypedDict, total=False):
    biometric_signature: Required[Annotated[str, PropertyInfo(alias="biometricSignature")]]
    """One-time, base64 encoded biometric proof for verification."""

    biometric_type: Required[
        Annotated[
            Literal["fingerprint", "facial_recognition", "voice_recognition"], PropertyInfo(alias="biometricType")
        ]
    ]
    """Type of biometric data for verification."""

    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]
    """The ID of the device from which the biometric verification attempt is made."""
