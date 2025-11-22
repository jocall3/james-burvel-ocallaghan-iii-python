# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.ai.advisor import (
    ChatSendMessageResponse,
    ChatRetrieveHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_history(self, client: JamesBurvelOcallaghanIii) -> None:
        chat = client.ai.advisor.chat.retrieve_history()
        assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_history_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        chat = client.ai.advisor.chat.retrieve_history(
            limit=10,
            offset=0,
            session_id="session-quantum-xyz-789-alpha",
        )
        assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_history(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.advisor.chat.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_history(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.advisor.chat.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message(self, client: JamesBurvelOcallaghanIii) -> None:
        chat = client.ai.advisor.chat.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        chat = client.ai.advisor.chat.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
            function_response={
                "name": "send_money",
                "response": {
                    "status": "success",
                    "transactionId": "pmt_654321",
                    "amountSent": 50,
                    "recipient": "Alex",
                },
            },
            session_id="session-quantum-xyz-789-alpha",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.advisor.chat.with_raw_response.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.advisor.chat.with_streaming_response.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_history(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        chat = await async_client.ai.advisor.chat.retrieve_history()
        assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_history_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        chat = await async_client.ai.advisor.chat.retrieve_history(
            limit=10,
            offset=0,
            session_id="session-quantum-xyz-789-alpha",
        )
        assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_history(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.advisor.chat.with_raw_response.retrieve_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_history(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.advisor.chat.with_streaming_response.retrieve_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatRetrieveHistoryResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        chat = await async_client.ai.advisor.chat.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        chat = await async_client.ai.advisor.chat.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
            function_response={
                "name": "send_money",
                "response": {
                    "status": "success",
                    "transactionId": "pmt_654321",
                    "amountSent": 50,
                    "recipient": "Alex",
                },
            },
            session_id="session-quantum-xyz-789-alpha",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.advisor.chat.with_raw_response.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.advisor.chat.with_streaming_response.send_message(
            message="Can you analyze my recent spending patterns and suggest areas for saving, focusing on my dining expenses?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
