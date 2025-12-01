# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FraudRuleActionParam"]


class FraudRuleActionParam(TypedDict, total=False):
    details: Required[str]
    """Details or instructions for the action."""

    type: Required[Literal["block", "alert", "auto_review", "manual_review", "request_mfa"]]
    """Type of action to perform."""

    target_team: Annotated[Optional[str], PropertyInfo(alias="targetTeam")]
    """The team or department to notify for alerts/reviews."""
