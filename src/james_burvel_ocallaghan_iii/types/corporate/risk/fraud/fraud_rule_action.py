# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FraudRuleAction"]


class FraudRuleAction(BaseModel):
    """Action to take when a fraud rule is triggered."""

    details: object
    """Details or instructions for the action."""

    type: Literal["block", "alert", "auto_review", "manual_review", "request_mfa"]
    """Type of action to perform."""

    target_team: Optional[object] = FieldInfo(alias="targetTeam", default=None)
    """The team or department to notify for alerts/reviews."""
