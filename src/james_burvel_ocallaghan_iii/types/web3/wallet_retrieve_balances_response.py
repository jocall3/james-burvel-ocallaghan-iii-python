# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WalletRetrieveBalancesResponse", "Data"]


class Data(BaseModel):
    asset_name: str = FieldInfo(alias="assetName")
    """Full name of the crypto asset."""

    asset_symbol: str = FieldInfo(alias="assetSymbol")
    """Symbol of the crypto asset (e.g., ETH, BTC, USDC)."""

    balance: float
    """Current balance of the asset in the wallet."""

    usd_value: float = FieldInfo(alias="usdValue")
    """Current USD value of the asset balance."""

    contract_address: Optional[str] = FieldInfo(alias="contractAddress", default=None)
    """The contract address for ERC-20 tokens or similar."""

    network: Optional[str] = None
    """
    The blockchain network the asset resides on (if different from wallet's
    primary).
    """


class WalletRetrieveBalancesResponse(BaseModel):
    limit: int
    """The maximum number of items returned in the current page."""

    offset: int
    """The number of items skipped before the current page."""

    total: int
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
