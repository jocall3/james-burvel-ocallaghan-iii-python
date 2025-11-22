# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .fraud_rule_action import FraudRuleAction
from .fraud_rule_criteria import FraudRuleCriteria

__all__ = ["FraudRule"]


class FraudRule(BaseModel):
    id: str
    """Unique identifier for the fraud detection rule."""

    action: FraudRuleAction
    """Action to take when a fraud rule is triggered."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the rule was created."""

    created_by: str = FieldInfo(alias="createdBy")
    """Identifier of who created the rule (e.g., user ID, 'system:ai-risk-engine')."""

    criteria: FraudRuleCriteria
    """Criteria that define when a fraud rule should trigger."""

    description: str
    """Detailed description of what the rule detects."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the rule was last updated."""

    name: str
    """Name of the fraud rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Severity level when this rule is triggered."""

    status: Literal["active", "inactive", "draft"]
    """Current status of the rule."""
