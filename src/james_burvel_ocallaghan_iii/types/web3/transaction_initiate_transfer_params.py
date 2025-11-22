# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionInitiateTransferParams"]


class TransactionInitiateTransferParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of cryptocurrency to transfer."""

    asset_symbol: Required[Annotated[str, PropertyInfo(alias="assetSymbol")]]
    """Symbol of the crypto asset to transfer (e.g., ETH, USDC)."""

    blockchain_network: Required[Annotated[str, PropertyInfo(alias="blockchainNetwork")]]
    """The blockchain network for the transfer."""

    recipient_address: Required[Annotated[str, PropertyInfo(alias="recipientAddress")]]
    """The recipient's blockchain address."""

    source_wallet_id: Required[Annotated[str, PropertyInfo(alias="sourceWalletId")]]
    """ID of the connected wallet from which to send funds."""

    gas_price_gwei: Annotated[Optional[int], PropertyInfo(alias="gasPriceGwei")]
    """Optional: Gas price in Gwei for Ethereum-based transactions."""

    memo: Optional[str]
    """Optional: A short memo or note for the transaction."""
