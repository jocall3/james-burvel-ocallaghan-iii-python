# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleCreateParams", "Action"]


class RuleCreateParams(TypedDict, total=False):
    action: Required[Action]

    criteria: Required[object]
    """The dynamic object defining the conditions that trigger the rule."""

    description: Required[str]
    """Detailed description of what the rule should detect."""

    name: Required[str]
    """A descriptive name for the new rule."""

    severity: Required[Literal["Low", "Medium", "High", "Critical"]]
    """Severity level for anomalies detected by this rule."""

    status: Required[Literal["active", "inactive", "draft"]]
    """Initial status of the rule."""

    priority: Optional[int]
    """Optional: Priority level for rule evaluation."""


class Action(TypedDict, total=False):
    details: Required[str]
    """Further details about the action."""

    type: Required[Literal["flag", "alert", "block", "auto_review", "mfa_challenge"]]
    """The automated action to take when the rule is triggered."""
