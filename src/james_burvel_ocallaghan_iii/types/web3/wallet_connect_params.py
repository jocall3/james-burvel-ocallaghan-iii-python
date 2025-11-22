# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WalletConnectParams"]


class WalletConnectParams(TypedDict, total=False):
    blockchain_network: Required[
        Annotated[
            Literal["Ethereum", "Solana", "Polygon", "BinanceSmartChain", "Arbitrum", "Optimism", "other"],
            PropertyInfo(alias="blockchainNetwork"),
        ]
    ]
    """The primary blockchain network of the wallet."""

    signed_message: Required[Annotated[str, PropertyInfo(alias="signedMessage")]]
    """A message signed by the wallet to prove ownership (e.g., EIP-191)."""

    wallet_address: Required[Annotated[str, PropertyInfo(alias="walletAddress")]]
    """The public address of the cryptocurrency wallet."""

    wallet_provider: Required[Annotated[str, PropertyInfo(alias="walletProvider")]]
    """The name of the wallet provider."""

    grant_write_access: Annotated[bool, PropertyInfo(alias="grantWriteAccess")]
    """
    Set to true if write access (transaction initiation) is desired (requires
    further permissions).
    """
