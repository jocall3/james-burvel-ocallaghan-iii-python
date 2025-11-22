# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.developers import (
    WebhookListResponse,
    WebhookSubscription,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: JamesBurvelOcallaghanIii) -> None:
        webhook = client.developers.webhooks.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        webhook = client.developers.webhooks.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
            secret="my_custom_webhook_secret_123",
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.developers.webhooks.with_raw_response.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.developers.webhooks.with_streaming_response.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookSubscription, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: JamesBurvelOcallaghanIii) -> None:
        webhook = client.developers.webhooks.update(
            subscription_id="whsub_devtool_finance_events",
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        webhook = client.developers.webhooks.update(
            subscription_id="whsub_devtool_finance_events",
            callback_url="https://my-new-app.com/webhooks/demobank-events",
            events=["transaction.updated"],
            secret="my_new_webhook_secret_456",
            status="paused",
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.developers.webhooks.with_raw_response.update(
            subscription_id="whsub_devtool_finance_events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.developers.webhooks.with_streaming_response.update(
            subscription_id="whsub_devtool_finance_events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookSubscription, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.developers.webhooks.with_raw_response.update(
                subscription_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        webhook = client.developers.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.developers.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.developers.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        webhook = client.developers.webhooks.delete(
            "whsub_devtool_finance_events",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.developers.webhooks.with_raw_response.delete(
            "whsub_devtool_finance_events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.developers.webhooks.with_streaming_response.delete(
            "whsub_devtool_finance_events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.developers.webhooks.with_raw_response.delete(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        webhook = await async_client.developers.webhooks.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        webhook = await async_client.developers.webhooks.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
            secret="my_custom_webhook_secret_123",
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.developers.webhooks.with_raw_response.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.developers.webhooks.with_streaming_response.create(
            callback_url="https://my-analytics-app.com/webhooks/transactions",
            events=["transaction.created", "transaction.updated"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookSubscription, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        webhook = await async_client.developers.webhooks.update(
            subscription_id="whsub_devtool_finance_events",
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        webhook = await async_client.developers.webhooks.update(
            subscription_id="whsub_devtool_finance_events",
            callback_url="https://my-new-app.com/webhooks/demobank-events",
            events=["transaction.updated"],
            secret="my_new_webhook_secret_456",
            status="paused",
        )
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.developers.webhooks.with_raw_response.update(
            subscription_id="whsub_devtool_finance_events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookSubscription, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.developers.webhooks.with_streaming_response.update(
            subscription_id="whsub_devtool_finance_events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookSubscription, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.developers.webhooks.with_raw_response.update(
                subscription_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        webhook = await async_client.developers.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.developers.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.developers.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        webhook = await async_client.developers.webhooks.delete(
            "whsub_devtool_finance_events",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.developers.webhooks.with_raw_response.delete(
            "whsub_devtool_finance_events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.developers.webhooks.with_streaming_response.delete(
            "whsub_devtool_finance_events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.developers.webhooks.with_raw_response.delete(
                "",
            )
