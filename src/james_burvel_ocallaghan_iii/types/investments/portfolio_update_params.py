# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioUpdateParams", "TargetAllocation"]


class PortfolioUpdateParams(TypedDict, total=False):
    ai_rebalancing_frequency: Annotated[
        Literal["monthly", "quarterly", "semi_annually", "annually", "manual"],
        PropertyInfo(alias="aiRebalancingFrequency"),
    ]
    """Updated frequency for AI-driven portfolio rebalancing."""

    name: str
    """New name for the investment portfolio."""

    risk_tolerance: Annotated[
        Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"],
        PropertyInfo(alias="riskTolerance"),
    ]
    """Updated risk tolerance for this portfolio."""

    target_allocation: Annotated[Optional[TargetAllocation], PropertyInfo(alias="targetAllocation")]
    """Optional: Target asset allocation percentages for rebalancing."""


class TargetAllocation(TypedDict, total=False):
    bonds: float

    cash: float

    equities: float
