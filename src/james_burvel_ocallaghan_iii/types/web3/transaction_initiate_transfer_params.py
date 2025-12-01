# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionInitiateTransferParams"]


class TransactionInitiateTransferParams(TypedDict, total=False):
    amount: Required[object]
    """The amount of cryptocurrency to transfer."""

    asset_symbol: Required[Annotated[object, PropertyInfo(alias="assetSymbol")]]
    """Symbol of the crypto asset to transfer (e.g., ETH, USDC)."""

    blockchain_network: Required[Annotated[object, PropertyInfo(alias="blockchainNetwork")]]
    """The blockchain network for the transfer."""

    recipient_address: Required[Annotated[object, PropertyInfo(alias="recipientAddress")]]
    """The recipient's blockchain address."""

    source_wallet_id: Required[Annotated[object, PropertyInfo(alias="sourceWalletId")]]
    """ID of the connected wallet from which to send funds."""

    gas_price_gwei: Annotated[object, PropertyInfo(alias="gasPriceGwei")]
    """Optional: Gas price in Gwei for Ethereum-based transactions."""

    memo: object
    """Optional: A short memo or note for the transaction."""
