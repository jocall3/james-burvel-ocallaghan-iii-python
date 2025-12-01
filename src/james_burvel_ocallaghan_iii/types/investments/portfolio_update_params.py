# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioUpdateParams"]


class PortfolioUpdateParams(TypedDict, total=False):
    ai_rebalancing_frequency: Annotated[
        Optional[Literal["monthly", "quarterly", "semi_annually", "annually", "never"]],
        PropertyInfo(alias="aiRebalancingFrequency"),
    ]
    """Updated frequency for AI-driven rebalancing."""

    name: str
    """Updated name of the portfolio."""

    risk_tolerance: Annotated[
        Literal["conservative", "moderate", "aggressive", "very_aggressive"], PropertyInfo(alias="riskTolerance")
    ]
    """Updated risk tolerance for this portfolio. May trigger rebalancing."""
