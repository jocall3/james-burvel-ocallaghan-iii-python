# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["RuleUpdateParams", "Action"]


class RuleUpdateParams(TypedDict, total=False):
    action: Action
    """Updated action to take when the rule is triggered."""

    criteria: Dict[str, object]
    """Updated JSON object defining the trigger conditions."""

    description: str
    """Updated description."""

    name: str
    """Updated name of the rule."""

    severity: Literal["Low", "Medium", "High", "Critical"]
    """Updated default severity level."""

    status: Literal["active", "inactive", "draft"]
    """Updated status of the rule."""


class Action(TypedDict, total=False):
    details: str

    type: Literal["flag", "alert", "block", "auto_review"]
