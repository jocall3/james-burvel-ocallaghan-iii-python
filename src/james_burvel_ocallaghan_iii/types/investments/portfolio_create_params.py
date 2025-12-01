# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioCreateParams"]


class PortfolioCreateParams(TypedDict, total=False):
    currency: Required[str]
    """ISO 4217 currency code of the portfolio."""

    initial_investment: Required[Annotated[float, PropertyInfo(alias="initialInvestment")]]
    """Initial amount to invest into the portfolio."""

    name: Required[str]
    """Name for the new investment portfolio."""

    risk_tolerance: Required[
        Annotated[
            Literal["conservative", "moderate", "aggressive", "very_aggressive"], PropertyInfo(alias="riskTolerance")
        ]
    ]
    """Desired risk tolerance for this portfolio."""

    type: Required[Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"]]
    """General type or strategy of the portfolio."""

    ai_auto_allocate: Annotated[bool, PropertyInfo(alias="aiAutoAllocate")]
    """
    If true, AI will automatically allocate initial investment based on risk
    tolerance.
    """

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: ID of a linked account to fund the initial investment."""
