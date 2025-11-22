# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WalletConnectParams"]


class WalletConnectParams(TypedDict, total=False):
    blockchain_network: Required[
        Annotated[
            Literal["Ethereum", "Solana", "Polygon", "Binance Smart Chain", "Avalanche", "Arbitrum", "Optimism"],
            PropertyInfo(alias="blockchainNetwork"),
        ]
    ]
    """The blockchain network the wallet is on."""

    signed_message: Required[Annotated[str, PropertyInfo(alias="signedMessage")]]
    """
    A cryptographic signature proving ownership of the wallet address (e.g., EIP-191
    signature).
    """

    wallet_address: Required[Annotated[str, PropertyInfo(alias="walletAddress")]]
    """The public address of the wallet to connect."""

    wallet_provider: Required[
        Annotated[
            Literal["MetaMask", "Phantom", "Ledger", "TrustWallet", "CoinbaseWallet", "Other"],
            PropertyInfo(alias="walletProvider"),
        ]
    ]
    """The provider/type of the wallet."""

    grant_write_access: Annotated[bool, PropertyInfo(alias="grantWriteAccess")]
    """
    If true, requests write access to initiate transactions (requires additional
    user confirmation).
    """
