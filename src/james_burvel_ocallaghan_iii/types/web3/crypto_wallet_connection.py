# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoWalletConnection"]


class CryptoWalletConnection(BaseModel):
    id: str
    """Unique identifier for the wallet connection within ."""

    blockchain_network: Literal[
        "Ethereum", "Solana", "Polygon", "BinanceSmartChain", "Avalanche", "Arbitrum", "Optimism", "Bitcoin", "other"
    ] = FieldInfo(alias="blockchainNetwork")
    """The primary blockchain network associated with the wallet."""

    last_synced: Optional[datetime] = FieldInfo(alias="lastSynced", default=None)
    """Timestamp of the last successful synchronization with the blockchain."""

    read_access_granted: bool = FieldInfo(alias="readAccessGranted")
    """Indicates if read access (balances, NFTs) has been granted."""

    status: Literal["connected", "disconnected", "error", "pending_verification"]
    """Current connection status of the wallet."""

    wallet_address: str = FieldInfo(alias="walletAddress")
    """The public address of the cryptocurrency wallet."""

    wallet_provider: Literal["MetaMask", "Phantom", "Ledger", "Trezor", "CoinbaseWallet", "WalletConnect", "other"] = (
        FieldInfo(alias="walletProvider")
    )
    """The provider or type of the connected wallet."""

    write_access_granted: bool = FieldInfo(alias="writeAccessGranted")
    """Indicates if write access (transactions) has been granted and is active."""

    alias: Optional[str] = None
    """A user-defined alias for the wallet."""
