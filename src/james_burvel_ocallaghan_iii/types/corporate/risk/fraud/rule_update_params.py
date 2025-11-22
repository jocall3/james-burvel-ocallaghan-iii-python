# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["RuleUpdateParams", "Action"]


class RuleUpdateParams(TypedDict, total=False):
    action: Action

    criteria: Dict[str, object]
    """The updated dynamic object defining the conditions."""

    description: str
    """Updated description of the rule."""

    name: str
    """Updated name for the fraud rule."""

    priority: Optional[int]
    """Updated priority level for rule evaluation."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Updated severity level."""

    status: Literal["active", "inactive", "draft"]
    """Updated status of the rule."""


class ActionTyped(TypedDict, total=False):
    details: str

    type: Literal["flag", "alert", "block", "auto_review", "mfa_challenge"]


Action: TypeAlias = Union[ActionTyped, Dict[str, object]]
