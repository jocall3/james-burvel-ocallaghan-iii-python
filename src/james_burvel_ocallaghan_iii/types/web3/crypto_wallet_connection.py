# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoWalletConnection"]


class CryptoWalletConnection(BaseModel):
    id: str
    """Unique identifier for this wallet connection."""

    blockchain_network: Literal[
        "Ethereum", "Solana", "Polygon", "BinanceSmartChain", "Arbitrum", "Optimism", "other"
    ] = FieldInfo(alias="blockchainNetwork")
    """The primary blockchain network this wallet is connected to."""

    last_synced: datetime = FieldInfo(alias="lastSynced")
    """Timestamp of the last successful synchronization of wallet data."""

    read_access_granted: bool = FieldInfo(alias="readAccessGranted")
    """Indicates if has permission to read balances and transaction history."""

    status: Literal["connected", "disconnected", "verification_pending", "error"]
    """Current status of the wallet connection."""

    wallet_address: str = FieldInfo(alias="walletAddress")
    """The public address of the connected cryptocurrency wallet."""

    wallet_provider: str = FieldInfo(alias="walletProvider")
    """The name of the wallet provider (e.g., MetaMask, Ledger, Phantom)."""

    write_access_granted: bool = FieldInfo(alias="writeAccessGranted")
    """
    Indicates if has permission to initiate transactions requiring user
    confirmation.
    """
