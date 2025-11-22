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
from ...types.web3 import wallet_connect_params
from ..._base_client import make_request_options
from ...types.web3.wallet_list_response import WalletListResponse
from ...types.web3.crypto_wallet_connection import CryptoWalletConnection
from ...types.web3.wallet_retrieve_balances_response import WalletRetrieveBalancesResponse

__all__ = ["WalletsResource", "AsyncWalletsResource"]


class WalletsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return WalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return WalletsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletListResponse:
        """
        Retrieves a list of all securely linked cryptocurrency wallets (e.g., MetaMask,
        Ledger integration), showing their addresses, associated networks, and
        verification status.
        """
        return self._get(
            "/web3/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletListResponse,
        )

    def connect(
        self,
        *,
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
        signed_message: str,
        wallet_address: str,
        wallet_provider: Literal["MetaMask", "Phantom", "Ledger", "Trezor", "CoinbaseWallet", "WalletConnect", "other"],
        message_to_sign: Optional[str] | Omit = omit,
        read_access: bool | Omit = omit,
        write_access: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoWalletConnection:
        """
        Initiates the process to securely connect a new cryptocurrency wallet to the
        user's profile, typically involving a signed message or OAuth flow from the
        wallet provider.

        Args:
          blockchain_network: The primary blockchain network for this wallet.

          signed_message: A cryptographic signature from the wallet, proving ownership or consent to
              connect.

          wallet_address: The public address of the cryptocurrency wallet.

          wallet_provider: The provider or type of the wallet being connected.

          message_to_sign: Optional: The original message that was signed, if provided by the client.

          read_access: Request for read access to wallet balances and NFTs.

          write_access: Request for write access to initiate transactions (requires further security
              layers).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web3/wallets",
            body=maybe_transform(
                {
                    "blockchain_network": blockchain_network,
                    "signed_message": signed_message,
                    "wallet_address": wallet_address,
                    "wallet_provider": wallet_provider,
                    "message_to_sign": message_to_sign,
                    "read_access": read_access,
                    "write_access": write_access,
                },
                wallet_connect_params.WalletConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CryptoWalletConnection,
        )

    def retrieve_balances(
        self,
        wallet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRetrieveBalancesResponse:
        """
        Retrieves the current balances of all recognized crypto assets within a specific
        connected wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return self._get(
            f"/web3/wallets/{wallet_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletRetrieveBalancesResponse,
        )


class AsyncWalletsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncWalletsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletListResponse:
        """
        Retrieves a list of all securely linked cryptocurrency wallets (e.g., MetaMask,
        Ledger integration), showing their addresses, associated networks, and
        verification status.
        """
        return await self._get(
            "/web3/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletListResponse,
        )

    async def connect(
        self,
        *,
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
        signed_message: str,
        wallet_address: str,
        wallet_provider: Literal["MetaMask", "Phantom", "Ledger", "Trezor", "CoinbaseWallet", "WalletConnect", "other"],
        message_to_sign: Optional[str] | Omit = omit,
        read_access: bool | Omit = omit,
        write_access: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoWalletConnection:
        """
        Initiates the process to securely connect a new cryptocurrency wallet to the
        user's profile, typically involving a signed message or OAuth flow from the
        wallet provider.

        Args:
          blockchain_network: The primary blockchain network for this wallet.

          signed_message: A cryptographic signature from the wallet, proving ownership or consent to
              connect.

          wallet_address: The public address of the cryptocurrency wallet.

          wallet_provider: The provider or type of the wallet being connected.

          message_to_sign: Optional: The original message that was signed, if provided by the client.

          read_access: Request for read access to wallet balances and NFTs.

          write_access: Request for write access to initiate transactions (requires further security
              layers).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web3/wallets",
            body=await async_maybe_transform(
                {
                    "blockchain_network": blockchain_network,
                    "signed_message": signed_message,
                    "wallet_address": wallet_address,
                    "wallet_provider": wallet_provider,
                    "message_to_sign": message_to_sign,
                    "read_access": read_access,
                    "write_access": write_access,
                },
                wallet_connect_params.WalletConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CryptoWalletConnection,
        )

    async def retrieve_balances(
        self,
        wallet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WalletRetrieveBalancesResponse:
        """
        Retrieves the current balances of all recognized crypto assets within a specific
        connected wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not wallet_id:
            raise ValueError(f"Expected a non-empty value for `wallet_id` but received {wallet_id!r}")
        return await self._get(
            f"/web3/wallets/{wallet_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletRetrieveBalancesResponse,
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_raw_response_wrapper(
            wallets.list,
        )
        self.connect = to_raw_response_wrapper(
            wallets.connect,
        )
        self.retrieve_balances = to_raw_response_wrapper(
            wallets.retrieve_balances,
        )


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_raw_response_wrapper(
            wallets.list,
        )
        self.connect = async_to_raw_response_wrapper(
            wallets.connect,
        )
        self.retrieve_balances = async_to_raw_response_wrapper(
            wallets.retrieve_balances,
        )


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_streamed_response_wrapper(
            wallets.list,
        )
        self.connect = to_streamed_response_wrapper(
            wallets.connect,
        )
        self.retrieve_balances = to_streamed_response_wrapper(
            wallets.retrieve_balances,
        )


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_streamed_response_wrapper(
            wallets.list,
        )
        self.connect = async_to_streamed_response_wrapper(
            wallets.connect,
        )
        self.retrieve_balances = async_to_streamed_response_wrapper(
            wallets.retrieve_balances,
        )
