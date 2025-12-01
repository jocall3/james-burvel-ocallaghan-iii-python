# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .fraud_rule_action_param import FraudRuleActionParam
from .fraud_rule_criteria_param import FraudRuleCriteriaParam

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    action: Required[FraudRuleActionParam]
    """Action to take when a fraud rule is triggered."""

    criteria: Required[FraudRuleCriteriaParam]
    """Criteria that define when a fraud rule should trigger."""

    description: Required[str]
    """Detailed description of what the rule detects."""

    name: Required[str]
    """Name of the new fraud rule."""

    severity: Required[Literal["Low", "Medium", "High", "Critical"]]
    """Severity level when this rule is triggered."""

    status: Required[Literal["active", "inactive", "draft"]]
    """Initial status of the rule."""
