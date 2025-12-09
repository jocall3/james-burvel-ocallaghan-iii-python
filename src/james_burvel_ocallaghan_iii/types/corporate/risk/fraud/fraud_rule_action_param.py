# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FraudRuleActionParam"]


class FraudRuleActionParam(TypedDict, total=False):
    """Action to take when a fraud rule is triggered."""

    details: Required[object]
    """Details or instructions for the action."""

    type: Required[Literal["block", "alert", "auto_review", "manual_review", "request_mfa"]]
    """Type of action to perform."""

    target_team: Annotated[object, PropertyInfo(alias="targetTeam")]
    """The team or department to notify for alerts/reviews."""
