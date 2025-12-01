# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WalletConnectParams"]


class WalletConnectParams(TypedDict, total=False):
    blockchain_network: Required[Annotated[str, PropertyInfo(alias="blockchainNetwork")]]
    """The blockchain network for this wallet (e.g., Ethereum, Solana)."""

    signed_message: Required[Annotated[str, PropertyInfo(alias="signedMessage")]]
    """
    A message cryptographically signed by the wallet owner to prove
    ownership/intent.
    """

    wallet_address: Required[Annotated[str, PropertyInfo(alias="walletAddress")]]
    """The public address of the cryptocurrency wallet."""

    wallet_provider: Required[Annotated[str, PropertyInfo(alias="walletProvider")]]
    """The name of the wallet provider (e.g., MetaMask, Phantom)."""

    request_write_access: Annotated[bool, PropertyInfo(alias="requestWriteAccess")]
    """If true, requests write access to initiate transactions from this wallet."""
