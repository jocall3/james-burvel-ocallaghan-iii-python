# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GoalUpdateParams"]


class GoalUpdateParams(TypedDict, total=False):
    name: str
    """Updated name of the financial goal."""

    regenerate_ai_plan: Annotated[bool, PropertyInfo(alias="regenerateAIPlan")]
    """If true, the AI will regenerate the strategic plan based on updated parameters."""

    risk_tolerance: Annotated[
        Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"],
        PropertyInfo(alias="riskTolerance"),
    ]
    """Updated risk tolerance for the investments associated with this goal."""

    status: Literal["on_track", "ahead_of_schedule", "behind_schedule", "completed", "cancelled"]
    """Updated status of the goal's progress."""

    target_amount: Annotated[float, PropertyInfo(alias="targetAmount")]
    """Updated target amount for the goal."""

    target_date: Annotated[Union[str, date], PropertyInfo(alias="targetDate", format="iso8601")]
    """Updated target completion date for the goal."""
