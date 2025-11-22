# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioRebalanceParams", "TargetAssetAllocation"]


class PortfolioRebalanceParams(TypedDict, total=False):
    target_risk_tolerance: Required[
        Annotated[Literal["low", "medium", "aggressive", "very_aggressive"], PropertyInfo(alias="targetRiskTolerance")]
    ]
    """The desired risk tolerance to rebalance the portfolio to."""

    confirmation_required: Annotated[bool, PropertyInfo(alias="confirmationRequired")]
    """If true, user confirmation is required before executing trades.

    Only applicable if dryRun is false.
    """

    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]
    """If true, the AI will only propose trades without executing them.

    Default is false.
    """

    target_asset_allocation: Annotated[
        Optional[Iterable[TargetAssetAllocation]], PropertyInfo(alias="targetAssetAllocation")
    ]
    """
    Optional: Specific target asset allocation percentages if not relying solely on
    AI risk tolerance.
    """


class TargetAssetAllocation(TypedDict, total=False):
    asset_class: Annotated[str, PropertyInfo(alias="assetClass")]

    percentage: float
