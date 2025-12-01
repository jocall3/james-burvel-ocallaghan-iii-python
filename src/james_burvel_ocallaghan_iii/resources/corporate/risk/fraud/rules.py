# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.corporate.risk.fraud import (
    rule_list_params,
    rule_create_params,
    rule_update_params,
)
from .....types.corporate.risk.fraud.fraud_rule import FraudRule
from .....types.corporate.risk.fraud.rule_list_response import RuleListResponse
from .....types.corporate.risk.fraud.fraud_rule_action_param import FraudRuleActionParam
from .....types.corporate.risk.fraud.fraud_rule_criteria_param import FraudRuleCriteriaParam

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action: FraudRuleActionParam,
        criteria: FraudRuleCriteriaParam,
        description: object,
        name: object,
        severity: Literal["Low", "Medium", "High", "Critical"],
        status: Literal["active", "inactive", "draft"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FraudRule:
        """
        Creates a new custom AI-powered fraud detection rule, allowing organizations to
        define specific criteria, risk scores, and automated responses to evolving
        threat landscapes.

        Args:
          action: Action to take when a fraud rule is triggered.

          criteria: Criteria that define when a fraud rule should trigger.

          description: Detailed description of what the rule detects.

          name: Name of the new fraud rule.

          severity: Severity level when this rule is triggered.

          status: Initial status of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/risk/fraud/rules",
            body=maybe_transform(
                {
                    "action": action,
                    "criteria": criteria,
                    "description": description,
                    "name": name,
                    "severity": severity,
                    "status": status,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FraudRule,
        )

    def update(
        self,
        rule_id: object,
        *,
        action: FraudRuleActionParam | Omit = omit,
        criteria: FraudRuleCriteriaParam | Omit = omit,
        description: object | Omit = omit,
        name: object | Omit = omit,
        severity: Literal["Low", "Medium", "High", "Critical"] | Omit = omit,
        status: Literal["active", "inactive", "draft"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FraudRule:
        """
        Updates an existing custom AI-powered fraud detection rule, modifying its
        criteria, actions, or status.

        Args:
          action: Action to take when a fraud rule is triggered.

          criteria: Criteria that define when a fraud rule should trigger.

          description: Updated description of what the rule detects.

          name: Updated name of the fraud rule.

          severity: Updated severity level.

          status: Updated status of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/corporate/risk/fraud/rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "criteria": criteria,
                    "description": description,
                    "name": name,
                    "severity": severity,
                    "status": status,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FraudRule,
        )

    def list(
        self,
        *,
        limit: object | Omit = omit,
        offset: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleListResponse:
        """
        Retrieves a list of AI-powered fraud detection rules currently active for the
        organization, including their parameters, thresholds, and associated actions
        (e.g., flag, block, alert).

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/corporate/risk/fraud/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            cast_to=RuleListResponse,
        )

    def delete(
        self,
        rule_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific custom AI-powered fraud detection rule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/corporate/risk/fraud/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action: FraudRuleActionParam,
        criteria: FraudRuleCriteriaParam,
        description: object,
        name: object,
        severity: Literal["Low", "Medium", "High", "Critical"],
        status: Literal["active", "inactive", "draft"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FraudRule:
        """
        Creates a new custom AI-powered fraud detection rule, allowing organizations to
        define specific criteria, risk scores, and automated responses to evolving
        threat landscapes.

        Args:
          action: Action to take when a fraud rule is triggered.

          criteria: Criteria that define when a fraud rule should trigger.

          description: Detailed description of what the rule detects.

          name: Name of the new fraud rule.

          severity: Severity level when this rule is triggered.

          status: Initial status of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/risk/fraud/rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "criteria": criteria,
                    "description": description,
                    "name": name,
                    "severity": severity,
                    "status": status,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FraudRule,
        )

    async def update(
        self,
        rule_id: object,
        *,
        action: FraudRuleActionParam | Omit = omit,
        criteria: FraudRuleCriteriaParam | Omit = omit,
        description: object | Omit = omit,
        name: object | Omit = omit,
        severity: Literal["Low", "Medium", "High", "Critical"] | Omit = omit,
        status: Literal["active", "inactive", "draft"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FraudRule:
        """
        Updates an existing custom AI-powered fraud detection rule, modifying its
        criteria, actions, or status.

        Args:
          action: Action to take when a fraud rule is triggered.

          criteria: Criteria that define when a fraud rule should trigger.

          description: Updated description of what the rule detects.

          name: Updated name of the fraud rule.

          severity: Updated severity level.

          status: Updated status of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/corporate/risk/fraud/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "criteria": criteria,
                    "description": description,
                    "name": name,
                    "severity": severity,
                    "status": status,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FraudRule,
        )

    async def list(
        self,
        *,
        limit: object | Omit = omit,
        offset: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleListResponse:
        """
        Retrieves a list of AI-powered fraud detection rules currently active for the
        organization, including their parameters, thresholds, and associated actions
        (e.g., flag, block, alert).

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/corporate/risk/fraud/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            cast_to=RuleListResponse,
        )

    async def delete(
        self,
        rule_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific custom AI-powered fraud detection rule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/corporate/risk/fraud/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
