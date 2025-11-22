# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionInitiateTransferParams"]


class TransactionInitiateTransferParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of cryptocurrency to transfer."""

    asset_symbol: Required[Annotated[str, PropertyInfo(alias="assetSymbol")]]
    """The ticker symbol of the asset to transfer (e.g., ETH, BTC, USDC)."""

    blockchain_network: Required[
        Annotated[
            Literal["Ethereum", "Solana", "Polygon", "BinanceSmartChain", "Arbitrum", "Optimism", "other"],
            PropertyInfo(alias="blockchainNetwork"),
        ]
    ]
    """The blockchain network on which the transaction will occur."""

    recipient_address: Required[Annotated[str, PropertyInfo(alias="recipientAddress")]]
    """The recipient's cryptocurrency address."""

    source_wallet_id: Required[Annotated[str, PropertyInfo(alias="sourceWalletId")]]
    """The ID of the connected wallet from which to transfer."""

    gas_price_gwei: Annotated[Optional[float], PropertyInfo(alias="gasPriceGwei")]
    """Optional: Gas price in Gwei for Ethereum-based transactions."""

    memo: Optional[str]
    """
    Optional: A memo or note for the transaction (supported by some
    networks/assets).
    """
