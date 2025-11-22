# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WalletConnectParams"]


class WalletConnectParams(TypedDict, total=False):
    blockchain_network: Required[
        Annotated[
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
            ],
            PropertyInfo(alias="blockchainNetwork"),
        ]
    ]
    """The primary blockchain network for this wallet."""

    signed_message: Required[Annotated[str, PropertyInfo(alias="signedMessage")]]
    """
    A cryptographic signature from the wallet, proving ownership or consent to
    connect.
    """

    wallet_address: Required[Annotated[str, PropertyInfo(alias="walletAddress")]]
    """The public address of the cryptocurrency wallet."""

    wallet_provider: Required[
        Annotated[
            Literal["MetaMask", "Phantom", "Ledger", "Trezor", "CoinbaseWallet", "WalletConnect", "other"],
            PropertyInfo(alias="walletProvider"),
        ]
    ]
    """The provider or type of the wallet being connected."""

    message_to_sign: Annotated[Optional[str], PropertyInfo(alias="messageToSign")]
    """Optional: The original message that was signed, if provided by the client."""

    read_access: Annotated[bool, PropertyInfo(alias="readAccess")]
    """Request for read access to wallet balances and NFTs."""

    write_access: Annotated[bool, PropertyInfo(alias="writeAccess")]
    """
    Request for write access to initiate transactions (requires further security
    layers).
    """
