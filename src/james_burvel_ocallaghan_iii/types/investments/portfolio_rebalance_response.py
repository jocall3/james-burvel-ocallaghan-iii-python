# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortfolioRebalanceResponse", "ProposedTrade"]


class ProposedTrade(BaseModel):
    action: Optional[Literal["buy", "sell"]] = None

    estimated_price: Optional[object] = FieldInfo(alias="estimatedPrice", default=None)

    quantity: Optional[object] = None

    symbol: Optional[object] = None


class PortfolioRebalanceResponse(BaseModel):
    portfolio_id: object = FieldInfo(alias="portfolioId")
    """ID of the portfolio being rebalanced."""

    rebalance_id: object = FieldInfo(alias="rebalanceId")
    """Unique identifier for the rebalancing operation."""

    status: Literal["analyzing", "pending_confirmation", "executing_trades", "completed", "failed"]
    """Current status of the rebalancing operation."""

    status_message: object = FieldInfo(alias="statusMessage")
    """A descriptive message about the current rebalance status."""

    confirmation_expires_at: Optional[object] = FieldInfo(alias="confirmationExpiresAt", default=None)
    """
    Timestamp when the rebalance confirmation expires, if `confirmationRequired` is
    true.
    """

    confirmation_required: Optional[object] = FieldInfo(alias="confirmationRequired", default=None)
    """Indicates if user confirmation is required to proceed with trades."""

    estimated_impact: Optional[object] = FieldInfo(alias="estimatedImpact", default=None)
    """AI-estimated impact of the rebalance on the portfolio."""

    proposed_trades: Optional[List[ProposedTrade]] = FieldInfo(alias="proposedTrades", default=None)
    """
    List of proposed trades if `dryRun` was true and status is
    `pending_confirmation`.
    """
