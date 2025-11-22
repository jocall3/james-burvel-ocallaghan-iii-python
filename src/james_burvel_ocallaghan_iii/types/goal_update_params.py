# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GoalUpdateParams"]


class GoalUpdateParams(TypedDict, total=False):
    name: str
    """Updated name for the financial goal."""

    regenerate_ai_plan: Annotated[bool, PropertyInfo(alias="regenerateAIPlan")]
    """If true, the AI will regenerate the strategic plan based on updated parameters."""

    risk_tolerance: Annotated[
        Literal["low", "medium", "aggressive", "very_aggressive"], PropertyInfo(alias="riskTolerance")
    ]
    """Updated risk tolerance for the investment strategy."""

    status: Literal["on_track", "ahead_of_schedule", "behind_schedule", "achieved", "cancelled"]
    """Updated status of the goal's progress."""

    target_amount: Annotated[float, PropertyInfo(alias="targetAmount")]
    """The updated target amount for this goal."""

    target_date: Annotated[Union[str, date], PropertyInfo(alias="targetDate", format="iso8601")]
    """The updated target date for achieving the goal."""
