# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleCreateParams", "Action"]


class RuleCreateParams(TypedDict, total=False):
    action: Required[Action]
    """Action to take when the rule is triggered."""

    criteria: Required[Dict[str, object]]
    """JSON object defining the conditions to trigger the rule."""

    description: Required[str]
    """Description of what the rule will detect."""

    name: Required[str]
    """Name of the new fraud detection rule."""

    severity: Required[Literal["Low", "Medium", "High", "Critical"]]
    """Default severity for anomalies detected by this rule."""

    status: Required[Literal["active", "inactive", "draft"]]
    """Initial status of the rule."""


class Action(TypedDict, total=False):
    details: str

    type: Literal["flag", "alert", "block", "auto_review"]
