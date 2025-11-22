# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BiometricVerifyResponse"]


class BiometricVerifyResponse(BaseModel):
    message: Optional[str] = None
    """A descriptive message for the verification result."""

    verification_status: Optional[Literal["success", "failed"]] = FieldInfo(alias="verificationStatus", default=None)
    """Status of the biometric verification."""
