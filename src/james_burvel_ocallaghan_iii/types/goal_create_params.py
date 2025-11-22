# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["GoalCreateParams"]


class GoalCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for the new financial goal."""

    risk_tolerance: Required[
        Annotated[Literal["low", "medium", "aggressive", "very_aggressive"], PropertyInfo(alias="riskTolerance")]
    ]
    """The risk tolerance for the investment strategy associated with this goal."""

    target_amount: Required[Annotated[float, PropertyInfo(alias="targetAmount")]]
    """The target amount to save/invest for this goal."""

    target_date: Required[Annotated[Union[str, date], PropertyInfo(alias="targetDate", format="iso8601")]]
    """The target date by which to achieve the goal."""

    type: Required[
        Literal[
            "retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "investment_growth", "other"
        ]
    ]
    """Type of financial goal."""

    generate_ai_plan: Annotated[bool, PropertyInfo(alias="generateAIPlan")]
    """If true, AI will automatically generate a strategic plan for this goal."""

    initial_contribution: Annotated[float, PropertyInfo(alias="initialContribution")]
    """Optional: Initial amount to contribute to this goal."""

    linked_account_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="linkedAccountIds")]
    """Optional: List of accounts to associate with this goal for contributions."""
