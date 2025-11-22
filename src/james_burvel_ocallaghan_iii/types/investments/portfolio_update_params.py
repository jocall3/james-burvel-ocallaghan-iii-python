# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioUpdateParams"]


class PortfolioUpdateParams(TypedDict, total=False):
    ai_rebalancing_frequency: Annotated[
        Literal["never", "monthly", "quarterly", "annually"], PropertyInfo(alias="aiRebalancingFrequency")
    ]
    """Updated frequency for AI-driven rebalancing."""

    name: str
    """Updated name of the portfolio."""

    risk_tolerance: Annotated[
        Literal["conservative", "balanced", "medium", "aggressive", "speculative"], PropertyInfo(alias="riskTolerance")
    ]
    """Updated risk tolerance for this portfolio."""
