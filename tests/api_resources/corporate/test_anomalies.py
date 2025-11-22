# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii._utils import parse_date
from james_burvel_ocallaghan_iii.types.corporate import (
    FinancialAnomaly,
    AnomalyListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnomalies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        anomaly = client.corporate.anomalies.list()
        assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        anomaly = client.corporate.anomalies.list(
            end_date=parse_date("2024-12-31"),
            entity_type="Transaction",
            limit=50,
            offset=0,
            severity="Critical",
            start_date=parse_date("2024-01-01"),
            status="New",
        )
        assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.anomalies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        anomaly = response.parse()
        assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.anomalies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            anomaly = response.parse()
            assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status(self, client: JamesBurvelOcallaghanIii) -> None:
        anomaly = client.corporate.anomalies.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
        )
        assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        anomaly = client.corporate.anomalies.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
            resolution_notes="Confirmed legitimate transaction after contacting vendor. Marked as resolved.",
        )
        assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.anomalies.with_raw_response.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        anomaly = response.parse()
        assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.anomalies.with_streaming_response.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            anomaly = response.parse()
            assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `anomaly_id` but received ''"):
            client.corporate.anomalies.with_raw_response.update_status(
                anomaly_id="",
                status="Resolved",
            )


class TestAsyncAnomalies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        anomaly = await async_client.corporate.anomalies.list()
        assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        anomaly = await async_client.corporate.anomalies.list(
            end_date=parse_date("2024-12-31"),
            entity_type="Transaction",
            limit=50,
            offset=0,
            severity="Critical",
            start_date=parse_date("2024-01-01"),
            status="New",
        )
        assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.anomalies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        anomaly = await response.parse()
        assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.anomalies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            anomaly = await response.parse()
            assert_matches_type(AnomalyListResponse, anomaly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        anomaly = await async_client.corporate.anomalies.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
        )
        assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        anomaly = await async_client.corporate.anomalies.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
            resolution_notes="Confirmed legitimate transaction after contacting vendor. Marked as resolved.",
        )
        assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.anomalies.with_raw_response.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        anomaly = await response.parse()
        assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.anomalies.with_streaming_response.update_status(
            anomaly_id="anom_risk-2024-07-21-D1E2F3",
            status="Resolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            anomaly = await response.parse()
            assert_matches_type(FinancialAnomaly, anomaly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `anomaly_id` but received ''"):
            await async_client.corporate.anomalies.with_raw_response.update_status(
                anomaly_id="",
                status="Resolved",
            )
