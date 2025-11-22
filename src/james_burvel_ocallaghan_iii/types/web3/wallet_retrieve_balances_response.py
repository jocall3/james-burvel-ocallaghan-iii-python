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
    """Ticker symbol of the cryptocurrency."""

    balance: float
    """Current balance of the asset in the wallet."""

    usd_value: Optional[float] = FieldInfo(alias="usdValue", default=None)
    """Estimated USD value of the balance."""

    blockchain_network: Optional[
        Literal["Ethereum", "Solana", "Polygon", "Binance Smart Chain", "Avalanche", "Arbitrum", "Optimism"]
    ] = FieldInfo(alias="blockchainNetwork", default=None)
    """The blockchain network of the asset."""

    contract_address: Optional[str] = FieldInfo(alias="contractAddress", default=None)
    """The contract address for ERC-20 tokens, if applicable."""


WalletRetrieveBalancesResponse: TypeAlias = List[WalletRetrieveBalancesResponseItem]
