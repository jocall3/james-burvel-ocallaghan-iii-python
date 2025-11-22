# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoWalletConnection"]


class CryptoWalletConnection(BaseModel):
    id: str
    """Unique identifier for this wallet connection."""

    blockchain_network: Literal[
        "Ethereum", "Solana", "Polygon", "Binance Smart Chain", "Avalanche", "Arbitrum", "Optimism"
    ] = FieldInfo(alias="blockchainNetwork")
    """The blockchain network this wallet connection is primarily on."""

    last_synced: datetime = FieldInfo(alias="lastSynced")
    """Timestamp of the last successful synchronization with the wallet."""

    read_access_granted: bool = FieldInfo(alias="readAccessGranted")
    """Indicates if read-only access to wallet data (balances, NFTs) is granted."""

    status: Literal["connected", "disconnected", "reconnect_required", "revoked"]
    """Current status of the wallet connection."""

    wallet_address: str = FieldInfo(alias="walletAddress")
    """The primary public address of the connected wallet."""

    wallet_provider: str = FieldInfo(alias="walletProvider")
    """Name of the wallet provider (e.g., MetaMask, Ledger, Phantom)."""

    write_access_granted: bool = FieldInfo(alias="writeAccessGranted")
    """Indicates if write access (e.g., to initiate transactions) is granted."""

    connection_type: Optional[Literal["direct", "walletconnect", "oauth", "api_key"]] = FieldInfo(
        alias="connectionType", default=None
    )
    """The technical method used for connecting the wallet."""
