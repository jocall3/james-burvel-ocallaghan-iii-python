# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionInitiateTransferParams"]


class TransactionInitiateTransferParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of crypto asset to transfer."""

    asset_symbol: Required[Annotated[str, PropertyInfo(alias="assetSymbol")]]
    """The ticker symbol of the crypto asset (e.g., ETH, USDC)."""

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
    """The blockchain network on which to execute the transfer."""

    recipient_address: Required[Annotated[str, PropertyInfo(alias="recipientAddress")]]
    """The public blockchain address of the recipient."""

    source_wallet_id: Required[Annotated[str, PropertyInfo(alias="sourceWalletId")]]
    """The ID of the connected wallet from which to send funds."""

    gas_price_gwei: Annotated[Optional[int], PropertyInfo(alias="gasPriceGwei")]
    """Optional: Desired gas price in Gwei for Ethereum-based transactions."""

    memo: Optional[str]
    """
    Optional: A short memo or note to include with the transaction (if supported by
    network).
    """
