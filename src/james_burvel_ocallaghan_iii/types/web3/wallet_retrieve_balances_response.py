# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WalletRetrieveBalancesResponse", "WalletRetrieveBalancesResponseItem"]


class WalletRetrieveBalancesResponseItem(BaseModel):
    asset_name: str = FieldInfo(alias="assetName")
    """Full name of the cryptocurrency asset."""

    asset_symbol: str = FieldInfo(alias="assetSymbol")
    """Ticker symbol of the cryptocurrency asset."""

    balance: float
    """Current balance of the asset in the wallet."""

    usd_value: float = FieldInfo(alias="usdValue")
    """Estimated USD value of the asset balance."""

    blockchain_network: Optional[
        Literal[
            "Ethereum",
            "Solana",
            "Polygon",
            "BinanceSmartChain",
            "Avalanche",
            "Arbitrum",
            "Optimism",
            "Bitcoin",
            "other",
        ]
    ] = FieldInfo(alias="blockchainNetwork", default=None)
    """The blockchain network this asset belongs to."""

    contract_address: Optional[str] = FieldInfo(alias="contractAddress", default=None)
    """The smart contract address for ERC-20 tokens or similar."""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when the balance was last updated/synced."""


WalletRetrieveBalancesResponse: TypeAlias = List[WalletRetrieveBalancesResponseItem]
