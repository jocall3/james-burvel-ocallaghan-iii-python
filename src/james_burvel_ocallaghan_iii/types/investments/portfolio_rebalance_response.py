# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortfolioRebalanceResponse", "ProposedTrade"]


class ProposedTrade(BaseModel):
    action: Optional[Literal["buy", "sell"]] = None

    estimated_cost_revenue: Optional[float] = FieldInfo(alias="estimatedCostRevenue", default=None)

    quantity: Optional[float] = None

    symbol: Optional[str] = None


class PortfolioRebalanceResponse(BaseModel):
    portfolio_id: str = FieldInfo(alias="portfolioId")
    """The ID of the portfolio being rebalanced."""

    rebalance_id: str = FieldInfo(alias="rebalanceId")
    """Unique identifier for the rebalancing operation."""

    status: Literal["analyzing", "pending_confirmation", "executing", "completed", "failed", "cancelled"]
    """Current status of the rebalancing operation."""

    status_message: str = FieldInfo(alias="statusMessage")
    """A descriptive message about the current status."""

    confirmation_expires_at: Optional[datetime] = FieldInfo(alias="confirmationExpiresAt", default=None)
    """Timestamp when pending confirmation will expire."""

    confirmation_required: Optional[bool] = FieldInfo(alias="confirmationRequired", default=None)
    """Indicates if user confirmation is needed to proceed with trades."""

    estimated_impact: Optional[str] = FieldInfo(alias="estimatedImpact", default=None)
    """AI's estimated impact of the rebalancing on portfolio metrics."""

    proposed_trades: Optional[List[ProposedTrade]] = FieldInfo(alias="proposedTrades", default=None)
    """Details of proposed trades if status is 'pending_confirmation' or 'executing'."""
