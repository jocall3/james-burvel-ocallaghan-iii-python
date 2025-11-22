# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioCreateParams"]


class PortfolioCreateParams(TypedDict, total=False):
    currency: Required[str]
    """Currency of the portfolio (ISO 4217 code)."""

    initial_investment: Required[Annotated[float, PropertyInfo(alias="initialInvestment")]]
    """Initial amount to invest in this portfolio."""

    name: Required[str]
    """Name for the new investment portfolio."""

    risk_tolerance: Required[
        Annotated[Literal["low", "medium", "aggressive", "very_aggressive"], PropertyInfo(alias="riskTolerance")]
    ]
    """Desired risk tolerance for this portfolio."""

    type: Required[Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"]]
    """Type of investment portfolio to create."""

    ai_auto_allocate: Annotated[bool, PropertyInfo(alias="aiAutoAllocate")]
    """
    If true, AI will automatically suggest and allocate initial assets based on risk
    tolerance.
    """

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: The account from which initial investment funds should be drawn."""
