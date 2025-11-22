# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["GoalUpdateParams"]


class GoalUpdateParams(TypedDict, total=False):
    contributing_accounts: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="contributingAccounts")]
    """Updated list of account IDs contributing to this goal."""

    generate_ai_plan: Annotated[bool, PropertyInfo(alias="generateAIPlan")]
    """If true, AI will recalculate and update the strategic plan for the goal."""

    name: str
    """Updated name of the financial goal."""

    risk_tolerance: Annotated[
        Optional[Literal["conservative", "moderate", "aggressive"]], PropertyInfo(alias="riskTolerance")
    ]
    """Updated risk tolerance for investments related to this goal."""

    status: Literal["on_track", "behind_schedule", "ahead_of_schedule", "completed", "paused", "cancelled"]
    """Updated status of the goal's progress."""

    target_amount: Annotated[float, PropertyInfo(alias="targetAmount")]
    """The updated target monetary amount for the goal."""

    target_date: Annotated[Union[str, date], PropertyInfo(alias="targetDate", format="iso8601")]
    """The updated target completion date for the goal."""
