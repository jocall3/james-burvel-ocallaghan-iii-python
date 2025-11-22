# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.web3 import transaction_initiate_transfer_params
from ..._base_client import make_request_options
from ...types.web3.transaction_initiate_transfer_response import TransactionInitiateTransferResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def initiate_transfer(
        self,
        *,
        amount: float,
        asset_symbol: str,
        blockchain_network: Literal[
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
        recipient_address: str,
        source_wallet_id: str,
        gas_price_gwei: Optional[int] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionInitiateTransferResponse:
        """
        Prepares and initiates a cryptocurrency transfer from a connected wallet to a
        specified recipient address. Requires user confirmation (e.g., via wallet
        signature).

        Args:
          amount: The amount of crypto asset to transfer.

          asset_symbol: The ticker symbol of the crypto asset (e.g., ETH, USDC).

          blockchain_network: The blockchain network on which to execute the transfer.

          recipient_address: The public blockchain address of the recipient.

          source_wallet_id: The ID of the connected wallet from which to send funds.

          gas_price_gwei: Optional: Desired gas price in Gwei for Ethereum-based transactions.

          memo: Optional: A short memo or note to include with the transaction (if supported by
              network).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web3/transactions/initiate",
            body=maybe_transform(
                {
                    "amount": amount,
                    "asset_symbol": asset_symbol,
                    "blockchain_network": blockchain_network,
                    "recipient_address": recipient_address,
                    "source_wallet_id": source_wallet_id,
                    "gas_price_gwei": gas_price_gwei,
                    "memo": memo,
                },
                transaction_initiate_transfer_params.TransactionInitiateTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionInitiateTransferResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def initiate_transfer(
        self,
        *,
        amount: float,
        asset_symbol: str,
        blockchain_network: Literal[
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
        recipient_address: str,
        source_wallet_id: str,
        gas_price_gwei: Optional[int] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionInitiateTransferResponse:
        """
        Prepares and initiates a cryptocurrency transfer from a connected wallet to a
        specified recipient address. Requires user confirmation (e.g., via wallet
        signature).

        Args:
          amount: The amount of crypto asset to transfer.

          asset_symbol: The ticker symbol of the crypto asset (e.g., ETH, USDC).

          blockchain_network: The blockchain network on which to execute the transfer.

          recipient_address: The public blockchain address of the recipient.

          source_wallet_id: The ID of the connected wallet from which to send funds.

          gas_price_gwei: Optional: Desired gas price in Gwei for Ethereum-based transactions.

          memo: Optional: A short memo or note to include with the transaction (if supported by
              network).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web3/transactions/initiate",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "asset_symbol": asset_symbol,
                    "blockchain_network": blockchain_network,
                    "recipient_address": recipient_address,
                    "source_wallet_id": source_wallet_id,
                    "gas_price_gwei": gas_price_gwei,
                    "memo": memo,
                },
                transaction_initiate_transfer_params.TransactionInitiateTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionInitiateTransferResponse,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.initiate_transfer = to_raw_response_wrapper(
            transactions.initiate_transfer,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.initiate_transfer = async_to_raw_response_wrapper(
            transactions.initiate_transfer,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.initiate_transfer = to_streamed_response_wrapper(
            transactions.initiate_transfer,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.initiate_transfer = async_to_streamed_response_wrapper(
            transactions.initiate_transfer,
        )
