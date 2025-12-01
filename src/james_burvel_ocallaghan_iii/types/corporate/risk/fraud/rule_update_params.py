# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .fraud_rule_action_param import FraudRuleActionParam
from .fraud_rule_criteria_param import FraudRuleCriteriaParam

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    action: FraudRuleActionParam
    """Updated action to take when the rule is triggered."""

    criteria: FraudRuleCriteriaParam
    """Updated criteria for the rule."""

    description: str
    """Updated description of what the rule detects."""

    name: str
    """Updated name of the fraud rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Updated severity level."""

    status: Literal["active", "inactive", "draft"]
    """Updated status of the rule."""
