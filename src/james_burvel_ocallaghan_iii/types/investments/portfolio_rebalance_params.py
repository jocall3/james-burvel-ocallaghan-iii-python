# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioRebalanceParams"]


class PortfolioRebalanceParams(TypedDict, total=False):
    target_risk_tolerance: Required[
        Annotated[
            Literal["conservative", "balanced", "medium", "aggressive", "speculative"],
            PropertyInfo(alias="targetRiskTolerance"),
        ]
    ]
    """The desired risk tolerance for the portfolio after rebalancing."""

    confirmation_required: Annotated[bool, PropertyInfo(alias="confirmationRequired")]
    """If true, explicit user confirmation is required before trades are executed."""

    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]
    """If true, the AI will only propose trades without executing them."""
