# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioRebalanceParams"]


class PortfolioRebalanceParams(TypedDict, total=False):
    confirmation_required: Annotated[bool, PropertyInfo(alias="confirmationRequired")]
    """
    If true, user confirmation is required before executing trades (even if dryRun
    is false).
    """

    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]
    """If true, the AI will only propose trades without executing them."""

    target_risk_tolerance: Annotated[
        Optional[Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"]],
        PropertyInfo(alias="targetRiskTolerance"),
    ]
    """Optional: The desired risk tolerance for the rebalancing.

    If not provided, uses portfolio's current risk tolerance.
    """
