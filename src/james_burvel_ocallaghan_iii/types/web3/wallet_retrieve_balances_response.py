# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WalletRetrieveBalancesResponse", "WalletRetrieveBalancesResponseItem"]


class WalletRetrieveBalancesResponseItem(BaseModel):
    asset_name: str = FieldInfo(alias="assetName")
    """Full name of the cryptocurrency."""

    asset_symbol: str = FieldInfo(alias="assetSymbol")
    """Ticker symbol of the cryptocurrency (e.g., ETH, BTC, USDC)."""

    balance: float
    """The current balance of the asset in the wallet."""

    usd_value: float = FieldInfo(alias="usdValue")
    """The equivalent value of the balance in USD."""

    blockchain_network: Optional[
        Literal["Ethereum", "Solana", "Polygon", "BinanceSmartChain", "Arbitrum", "Optimism", "other"]
    ] = FieldInfo(alias="blockchainNetwork", default=None)
    """The blockchain network where this asset resides."""

    contract_address: Optional[str] = FieldInfo(alias="contractAddress", default=None)
    """The contract address for ERC-20 tokens (if applicable)."""


WalletRetrieveBalancesResponse: TypeAlias = List[WalletRetrieveBalancesResponseItem]
