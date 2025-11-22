# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioCreateParams"]


class PortfolioCreateParams(TypedDict, total=False):
    currency: Required[str]
    """Base currency of the portfolio."""

    initial_investment: Required[Annotated[float, PropertyInfo(alias="initialInvestment")]]
    """Initial amount to invest in the portfolio."""

    name: Required[str]
    """Name for the new investment portfolio."""

    risk_tolerance: Required[
        Annotated[
            Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"],
            PropertyInfo(alias="riskTolerance"),
        ]
    ]
    """User's risk tolerance for this portfolio."""

    type: Required[Literal["equities", "bonds", "diversified", "crypto", "reit", "commodities", "other"]]
    """Primary asset type or strategy of the portfolio."""

    ai_auto_allocate: Annotated[bool, PropertyInfo(alias="aiAutoAllocate")]
    """
    If true, AI will automatically suggest and execute initial asset allocation
    based on risk tolerance.
    """

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: The account from which initial funds should be drawn."""
