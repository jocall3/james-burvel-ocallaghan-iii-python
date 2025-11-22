# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .crypto_wallet_connection import CryptoWalletConnection

__all__ = ["WalletListResponse"]

WalletListResponse: TypeAlias = List[CryptoWalletConnection]
