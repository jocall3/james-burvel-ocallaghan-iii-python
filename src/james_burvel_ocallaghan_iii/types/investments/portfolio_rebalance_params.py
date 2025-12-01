# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioRebalanceParams"]


class PortfolioRebalanceParams(TypedDict, total=False):
    target_risk_tolerance: Required[
        Annotated[
            Literal["conservative", "moderate", "aggressive", "very_aggressive"],
            PropertyInfo(alias="targetRiskTolerance"),
        ]
    ]
    """The desired risk tolerance for rebalancing the portfolio."""

    confirmation_required: Annotated[object, PropertyInfo(alias="confirmationRequired")]
    """
    If true, user confirmation is required before executing actual trades after a
    dry run.
    """

    dry_run: Annotated[object, PropertyInfo(alias="dryRun")]
    """If true, only simulate the rebalance without executing trades.

    Returns proposed trades.
    """
