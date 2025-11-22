# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioCreateParams"]


class PortfolioCreateParams(TypedDict, total=False):
    currency: Required[str]
    """The base currency of the portfolio."""

    initial_investment: Required[Annotated[float, PropertyInfo(alias="initialInvestment")]]
    """Initial amount to invest in this portfolio."""

    name: Required[str]
    """Name for the new investment portfolio."""

    risk_tolerance: Required[
        Annotated[
            Literal["conservative", "balanced", "medium", "aggressive", "speculative"],
            PropertyInfo(alias="riskTolerance"),
        ]
    ]
    """Desired risk tolerance for this portfolio."""

    type: Required[Literal["equities", "bonds", "diversified", "retirement", "crypto", "custom"]]
    """Type or strategy of the investment portfolio."""

    ai_auto_allocate: Annotated[bool, PropertyInfo(alias="aiAutoAllocate")]
    """
    If true, AI will automatically suggest and allocate assets based on risk
    tolerance.
    """

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: The ID of a linked bank account to draw initial investment from."""
