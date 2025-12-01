# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GoalCreateParams"]


class GoalCreateParams(TypedDict, total=False):
    name: Required[object]
    """Name of the new financial goal."""

    target_amount: Required[Annotated[object, PropertyInfo(alias="targetAmount")]]
    """The target monetary amount for the goal."""

    target_date: Required[Annotated[object, PropertyInfo(alias="targetDate")]]
    """The target completion date for the goal."""

    type: Required[Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "other"]]
    """Type of financial goal."""

    contributing_accounts: Annotated[Optional[Iterable[object]], PropertyInfo(alias="contributingAccounts")]
    """Optional: List of account IDs initially contributing to this goal."""

    generate_ai_plan: Annotated[object, PropertyInfo(alias="generateAIPlan")]
    """If true, AI will automatically generate a strategic plan for the goal."""

    initial_contribution: Annotated[object, PropertyInfo(alias="initialContribution")]
    """Optional: Initial amount to contribute to the goal."""

    risk_tolerance: Annotated[
        Optional[Literal["conservative", "moderate", "aggressive"]], PropertyInfo(alias="riskTolerance")
    ]
    """Desired risk tolerance for investments related to this goal."""
