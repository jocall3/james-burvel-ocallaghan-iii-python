# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoWalletConnection"]


class CryptoWalletConnection(BaseModel):
    id: object
    """Unique identifier for this wallet connection."""

    blockchain_network: object = FieldInfo(alias="blockchainNetwork")
    """
    The blockchain network this wallet is primarily connected to (e.g., Ethereum,
    Solana, Polygon).
    """

    last_synced: object = FieldInfo(alias="lastSynced")
    """Timestamp when the wallet's data was last synchronized."""

    read_access_granted: object = FieldInfo(alias="readAccessGranted")
    """Indicates if read access (balances, NFTs) is granted."""

    status: Literal["connected", "disconnected", "pending_verification", "error"]
    """Current status of the wallet connection."""

    wallet_address: object = FieldInfo(alias="walletAddress")
    """Public address of the connected cryptocurrency wallet."""

    wallet_provider: object = FieldInfo(alias="walletProvider")
    """Name of the wallet provider (e.g., MetaMask, Ledger, Phantom)."""

    write_access_granted: object = FieldInfo(alias="writeAccessGranted")
    """Indicates if write access (transactions) is granted.

    Requires higher permission/security.
    """
