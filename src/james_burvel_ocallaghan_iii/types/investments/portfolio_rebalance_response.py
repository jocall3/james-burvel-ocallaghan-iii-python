# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortfolioRebalanceResponse", "ProposedTrade"]


class ProposedTrade(BaseModel):
    action: Optional[Literal["buy", "sell"]] = None

    estimated_price: Optional[float] = FieldInfo(alias="estimatedPrice", default=None)

    quantity: Optional[float] = None

    symbol: Optional[str] = None


class PortfolioRebalanceResponse(BaseModel):
    portfolio_id: str = FieldInfo(alias="portfolioId")
    """ID of the portfolio being rebalanced."""

    rebalance_id: str = FieldInfo(alias="rebalanceId")
    """Unique identifier for the rebalancing operation."""

    status: Literal["analyzing", "pending_confirmation", "executing_trades", "completed", "failed"]
    """Current status of the rebalancing operation."""

    status_message: str = FieldInfo(alias="statusMessage")
    """A descriptive message about the current rebalance status."""

    confirmation_expires_at: Optional[datetime] = FieldInfo(alias="confirmationExpiresAt", default=None)
    """
    Timestamp when the rebalance confirmation expires, if `confirmationRequired` is
    true.
    """

    confirmation_required: Optional[bool] = FieldInfo(alias="confirmationRequired", default=None)
    """Indicates if user confirmation is required to proceed with trades."""

    estimated_impact: Optional[str] = FieldInfo(alias="estimatedImpact", default=None)
    """AI-estimated impact of the rebalance on the portfolio."""

    proposed_trades: Optional[List[ProposedTrade]] = FieldInfo(alias="proposedTrades", default=None)
    """
    List of proposed trades if `dryRun` was true and status is
    `pending_confirmation`.
    """
