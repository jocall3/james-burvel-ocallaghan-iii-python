# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.corporate.risk.fraud import (
    FraudRule,
    RuleListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: JamesBurvelOcallaghanIii) -> None:
        rule = client.corporate.risk.fraud.rules.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        rule = client.corporate.risk.fraud.rules.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
            priority=60,
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(FraudRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: JamesBurvelOcallaghanIii) -> None:
        rule = client.corporate.risk.fraud.rules.update(
            rule_id="fraud_rule_high_value_inactive",
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        rule = client.corporate.risk.fraud.rules.update(
            rule_id="fraud_rule_high_value_inactive",
            action={
                "details": "Flag for manual review only, do not block.",
                "type": "flag",
            },
            criteria={
                "transactionAmountMin": "bar",
                "accountInactivityDays": "bar",
            },
            description="Revised: Flags transactions over a higher threshold from dormant accounts.",
            name="Updated High Value Transaction Rule",
            priority=55,
            severity="High",
            status="inactive",
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.update(
            rule_id="fraud_rule_high_value_inactive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.update(
            rule_id="fraud_rule_high_value_inactive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(FraudRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.corporate.risk.fraud.rules.with_raw_response.update(
                rule_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        rule = client.corporate.risk.fraud.rules.list()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleListResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        rule = client.corporate.risk.fraud.rules.delete(
            "fraud_rule_high_value_inactive",
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.risk.fraud.rules.with_raw_response.delete(
            "fraud_rule_high_value_inactive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.risk.fraud.rules.with_streaming_response.delete(
            "fraud_rule_high_value_inactive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.corporate.risk.fraud.rules.with_raw_response.delete(
                "",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        rule = await async_client.corporate.risk.fraud.rules.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        rule = await async_client.corporate.risk.fraud.rules.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
            priority=60,
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.create(
            action={
                "details": "Hold payment, notify sender for additional verification, and escalate to compliance.",
                "type": "auto_review",
            },
            criteria={
                "paymentCountMin": 3,
                "timeframeHours": 24,
                "recipientNew": True,
                "recipientCountryRiskLevel": ["High", "Very High"],
            },
            description="Detects multiple international payments to new beneficiaries in high-risk countries within a short timeframe.",
            name="Suspicious International Payment Pattern",
            severity="Critical",
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(FraudRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        rule = await async_client.corporate.risk.fraud.rules.update(
            rule_id="fraud_rule_high_value_inactive",
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        rule = await async_client.corporate.risk.fraud.rules.update(
            rule_id="fraud_rule_high_value_inactive",
            action={
                "details": "Flag for manual review only, do not block.",
                "type": "flag",
            },
            criteria={
                "transactionAmountMin": "bar",
                "accountInactivityDays": "bar",
            },
            description="Revised: Flags transactions over a higher threshold from dormant accounts.",
            name="Updated High Value Transaction Rule",
            priority=55,
            severity="High",
            status="inactive",
        )
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.update(
            rule_id="fraud_rule_high_value_inactive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(FraudRule, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.update(
            rule_id="fraud_rule_high_value_inactive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(FraudRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.corporate.risk.fraud.rules.with_raw_response.update(
                rule_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        rule = await async_client.corporate.risk.fraud.rules.list()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleListResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        rule = await async_client.corporate.risk.fraud.rules.delete(
            "fraud_rule_high_value_inactive",
        )
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.risk.fraud.rules.with_raw_response.delete(
            "fraud_rule_high_value_inactive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.risk.fraud.rules.with_streaming_response.delete(
            "fraud_rule_high_value_inactive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.corporate.risk.fraud.rules.with_raw_response.delete(
                "",
            )
