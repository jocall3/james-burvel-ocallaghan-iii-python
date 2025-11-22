# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FraudRule", "Action"]


class Action(BaseModel):
    details: str
    """Further details about the action."""

    type: Literal["flag", "alert", "block", "auto_review", "mfa_challenge"]
    """The automated action to take when the rule is triggered."""


class FraudRule(BaseModel):
    id: str
    """Unique identifier for the fraud rule."""

    action: Action

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the rule was created."""

    created_by: str = FieldInfo(alias="createdBy")
    """Identifier of the creator (user or system)."""

    criteria: object
    """A dynamic object defining the conditions that trigger the rule."""

    description: str
    """Detailed description of what the rule detects."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the rule was last updated."""

    name: str
    """A descriptive name for the rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Severity level associated with a detected anomaly by this rule."""

    status: Literal["active", "inactive", "draft"]
    """Current status of the rule."""

    priority: Optional[int] = None
    """Priority level for rule evaluation (lower number means higher priority)."""
