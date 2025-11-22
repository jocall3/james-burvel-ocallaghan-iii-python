# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GoalCreateParams"]


class GoalCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for the new financial goal."""

    target_amount: Required[Annotated[float, PropertyInfo(alias="targetAmount")]]
    """The target amount for the goal."""

    target_date: Required[Annotated[Union[str, date], PropertyInfo(alias="targetDate", format="iso8601")]]
    """Target completion date for the goal."""

    type: Required[
        Literal[
            "retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "wealth_creation", "other"
        ]
    ]
    """Type of financial goal."""

    generate_ai_plan: Annotated[bool, PropertyInfo(alias="generateAIPlan")]
    """If true, AI will automatically generate a strategic plan for this goal."""

    initial_contribution: Annotated[float, PropertyInfo(alias="initialContribution")]
    """Optional: Initial amount to contribute to the goal."""

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: The account ID from which the initial contribution should be made."""

    risk_tolerance: Annotated[
        Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"],
        PropertyInfo(alias="riskTolerance"),
    ]
    """Risk tolerance for the investments associated with this goal."""
