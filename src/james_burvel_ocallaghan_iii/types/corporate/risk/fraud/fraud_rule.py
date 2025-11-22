# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FraudRule", "Action"]


class Action(BaseModel):
    details: Optional[str] = None

    type: Optional[Literal["flag", "alert", "block", "auto_review"]] = None


class FraudRule(BaseModel):
    id: str
    """Unique identifier for the fraud detection rule."""

    action: Action
    """The action to be taken when the rule is triggered."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the rule was created."""

    created_by: str = FieldInfo(alias="createdBy")
    """Identifier of the user or system that created the rule."""

    criteria: Dict[str, object]
    """A JSON object defining the specific conditions that trigger the rule."""

    description: str
    """Detailed description of what the rule detects."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the rule was last modified."""

    name: str
    """Human-readable name of the rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Default severity level assigned to anomalies detected by this rule."""

    status: Literal["active", "inactive", "draft"]
    """Current status of the rule."""
