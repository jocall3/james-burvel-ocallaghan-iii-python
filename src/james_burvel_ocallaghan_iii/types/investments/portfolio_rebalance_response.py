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
    """The ID of the portfolio being rebalanced."""

    rebalance_id: str = FieldInfo(alias="rebalanceId")
    """Unique identifier for the rebalancing operation."""

    status: Literal["analyzing", "proposed", "pending_confirmation", "executing", "completed", "failed"]
    """Current status of the rebalancing operation."""

    confirmation_expires_at: Optional[datetime] = FieldInfo(alias="confirmationExpiresAt", default=None)
    """Timestamp when the proposed rebalance expires if not confirmed."""

    confirmation_required: Optional[bool] = FieldInfo(alias="confirmationRequired", default=None)
    """Indicates if user confirmation is required before execution."""

    estimated_impact: Optional[str] = FieldInfo(alias="estimatedImpact", default=None)
    """AI's estimated impact of the rebalancing on portfolio metrics."""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp of the last status update."""

    proposed_trades: Optional[List[ProposedTrade]] = FieldInfo(alias="proposedTrades", default=None)
    """List of proposed buy/sell trades if status is 'proposed'."""

    status_message: Optional[str] = FieldInfo(alias="statusMessage", default=None)
    """A descriptive message about the current status."""
