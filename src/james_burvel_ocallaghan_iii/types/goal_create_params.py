# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GoalCreateParams"]


class GoalCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the new financial goal."""

    target_amount: Required[Annotated[float, PropertyInfo(alias="targetAmount")]]
    """The target amount to save or achieve."""

    target_date: Required[Annotated[Union[str, date], PropertyInfo(alias="targetDate", format="iso8601")]]
    """The target date for the goal."""

    type: Required[Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "custom"]]
    """Type of financial goal."""

    generate_ai_plan: Annotated[bool, PropertyInfo(alias="generateAIPlan")]
    """If true, AI will generate a strategic plan to achieve the goal."""

    initial_contribution: Annotated[float, PropertyInfo(alias="initialContribution")]
    """Optional: An initial amount contributed to the goal."""

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: The ID of a primary account to link for contributions."""

    risk_tolerance: Annotated[
        Literal["conservative", "balanced", "medium", "aggressive", "speculative"], PropertyInfo(alias="riskTolerance")
    ]
    """Risk tolerance for investments related to this goal."""
