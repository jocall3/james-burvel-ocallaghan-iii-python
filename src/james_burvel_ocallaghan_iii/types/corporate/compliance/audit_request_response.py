# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuditRequestResponse"]


class AuditRequestResponse(BaseModel):
    audit_id: Optional[str] = FieldInfo(alias="auditId", default=None)
    """Unique identifier for the initiated audit."""

    status: Optional[Literal["initiated", "processing", "completed", "failed"]] = None
    """Current status of the audit."""
