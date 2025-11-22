# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortfolioRebalanceResponse", "ProposedTrade"]


class ProposedTrade(BaseModel):
    action: Optional[Literal["buy", "sell"]] = None
    """Action to perform (buy/sell)."""

    asset_symbol: Optional[str] = FieldInfo(alias="assetSymbol", default=None)
    """Symbol of the asset to trade."""

    estimated_price: Optional[float] = FieldInfo(alias="estimatedPrice", default=None)
    """Estimated price per unit."""

    quantity: Optional[float] = None
    """Quantity of shares/units."""


class PortfolioRebalanceResponse(BaseModel):
    portfolio_id: str = FieldInfo(alias="portfolioId")
    """The ID of the portfolio being rebalanced."""

    rebalance_id: str = FieldInfo(alias="rebalanceId")
    """Unique ID for the rebalancing operation."""

    status: Literal["analyzing", "proposed", "pending_confirmation", "executing", "completed", "failed"]
    """Current status of the rebalancing operation."""

    status_message: str = FieldInfo(alias="statusMessage")
    """A descriptive message about the current status."""

    confirmation_expires_at: Optional[datetime] = FieldInfo(alias="confirmationExpiresAt", default=None)
    """Timestamp when the proposed trades will expire if not confirmed."""

    confirmation_required: Optional[bool] = FieldInfo(alias="confirmationRequired", default=None)
    """Indicates if user confirmation is pending for proposed trades."""

    estimated_impact: Optional[str] = FieldInfo(alias="estimatedImpact", default=None)
    """AI's estimated impact of the rebalancing on portfolio metrics."""

    proposed_trades: Optional[List[ProposedTrade]] = FieldInfo(alias="proposedTrades", default=None)
    """A list of proposed trades, if status is 'proposed' or 'pending_confirmation'."""
