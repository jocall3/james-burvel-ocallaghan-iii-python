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
    """The symbol of the cryptocurrency to transfer (e.g., ETH, USDC)."""

    blockchain_network: Required[
        Annotated[
            Literal["Ethereum", "Solana", "Polygon", "Binance Smart Chain", "Avalanche", "Arbitrum", "Optimism"],
            PropertyInfo(alias="blockchainNetwork"),
        ]
    ]
    """The blockchain network on which the transfer will occur."""

    recipient_address: Required[Annotated[str, PropertyInfo(alias="recipientAddress")]]
    """The recipient's blockchain address."""

    source_wallet_id: Required[Annotated[str, PropertyInfo(alias="sourceWalletId")]]
    """The ID of the connected wallet from which to transfer."""

    gas_limit: Annotated[Optional[int], PropertyInfo(alias="gasLimit")]
    """Optional: Maximum gas units to consume for the transaction."""

    gas_price_gwei: Annotated[Optional[float], PropertyInfo(alias="gasPriceGwei")]
    """Optional: Desired gas price in Gwei for Ethereum-based transactions."""

    memo: Optional[str]
    """Optional: A short memo or note for the transaction (supported by some chains)."""
