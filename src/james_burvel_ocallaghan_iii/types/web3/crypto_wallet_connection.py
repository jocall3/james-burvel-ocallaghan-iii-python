# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoWalletConnection"]


class CryptoWalletConnection(BaseModel):
    id: str
    """Unique identifier for this wallet connection."""

    blockchain_network: str = FieldInfo(alias="blockchainNetwork")
    """
    The blockchain network this wallet is primarily connected to (e.g., Ethereum,
    Solana, Polygon).
    """

    last_synced: datetime = FieldInfo(alias="lastSynced")
    """Timestamp when the wallet's data was last synchronized."""

    read_access_granted: bool = FieldInfo(alias="readAccessGranted")
    """Indicates if read access (balances, NFTs) is granted."""

    status: Literal["connected", "disconnected", "pending_verification", "error"]
    """Current status of the wallet connection."""

    wallet_address: str = FieldInfo(alias="walletAddress")
    """Public address of the connected cryptocurrency wallet."""

    wallet_provider: str = FieldInfo(alias="walletProvider")
    """Name of the wallet provider (e.g., MetaMask, Ledger, Phantom)."""

    write_access_granted: bool = FieldInfo(alias="writeAccessGranted")
    """Indicates if write access (transactions) is granted.

    Requires higher permission/security.
    """
