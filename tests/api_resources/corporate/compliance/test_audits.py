# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.corporate.compliance import (
    AuditRequestResponse,
    AuditRetrieveReportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_request(self, client: JamesBurvelOcallaghanIii) -> None:
        audit = client.corporate.compliance.audits.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
        )
        assert_matches_type(AuditRequestResponse, audit, path=["response"])

    @parametrize
    def test_method_request_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        audit = client.corporate.compliance.audits.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
            additional_context={},
        )
        assert_matches_type(AuditRequestResponse, audit, path=["response"])

    @parametrize
    def test_raw_response_request(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.compliance.audits.with_raw_response.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(AuditRequestResponse, audit, path=["response"])

    @parametrize
    def test_streaming_response_request(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.compliance.audits.with_streaming_response.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(AuditRequestResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_report(self, client: JamesBurvelOcallaghanIii) -> None:
        audit = client.corporate.compliance.audits.retrieve_report(
            "audit_corp_xyz789",
        )
        assert_matches_type(AuditRetrieveReportResponse, audit, path=["response"])

    @parametrize
    def test_raw_response_retrieve_report(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.compliance.audits.with_raw_response.retrieve_report(
            "audit_corp_xyz789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(AuditRetrieveReportResponse, audit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_report(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.compliance.audits.with_streaming_response.retrieve_report(
            "audit_corp_xyz789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(AuditRetrieveReportResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_request(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        audit = await async_client.corporate.compliance.audits.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
        )
        assert_matches_type(AuditRequestResponse, audit, path=["response"])

    @parametrize
    async def test_method_request_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        audit = await async_client.corporate.compliance.audits.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
            additional_context={},
        )
        assert_matches_type(AuditRequestResponse, audit, path=["response"])

    @parametrize
    async def test_raw_response_request(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.compliance.audits.with_raw_response.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AuditRequestResponse, audit, path=["response"])

    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.compliance.audits.with_streaming_response.request(
            audit_scope="all_transactions",
            end_date="2024-06-30",
            regulatory_frameworks=["AML", "PCI-DSS"],
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AuditRequestResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_report(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        audit = await async_client.corporate.compliance.audits.retrieve_report(
            "audit_corp_xyz789",
        )
        assert_matches_type(AuditRetrieveReportResponse, audit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_report(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.compliance.audits.with_raw_response.retrieve_report(
            "audit_corp_xyz789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AuditRetrieveReportResponse, audit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_report(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.compliance.audits.with_streaming_response.retrieve_report(
            "audit_corp_xyz789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AuditRetrieveReportResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True
