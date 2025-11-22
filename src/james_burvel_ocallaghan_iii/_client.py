# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import goals, budgets
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.ai import ai
from .resources.web3 import web3
from .resources.users import users
from .resources.lending import lending
from .resources.accounts import accounts
from .resources.identity import identity
from .resources.payments import payments
from .resources.corporate import corporate
from .resources.developers import developers
from .resources.investments import investments
from .resources.marketplace import marketplace
from .resources.transactions import transactions
from .resources.sustainability import sustainability

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "JamesBurvelOcallaghanIii",
    "AsyncJamesBurvelOcallaghanIii",
    "Client",
    "AsyncClient",
]


class JamesBurvelOcallaghanIii(SyncAPIClient):
    users: users.UsersResource
    accounts: accounts.AccountsResource
    transactions: transactions.TransactionsResource
    budgets: budgets.BudgetsResource
    investments: investments.InvestmentsResource
    ai: ai.AIResource
    corporate: corporate.CorporateResource
    web3: web3.Web3Resource
    payments: payments.PaymentsResource
    sustainability: sustainability.SustainabilityResource
    lending: lending.LendingResource
    developers: developers.DevelopersResource
    identity: identity.IdentityResource
    goals: goals.GoalsResource
    marketplace: marketplace.MarketplaceResource
    with_raw_response: JamesBurvelOcallaghanIiiWithRawResponse
    with_streaming_response: JamesBurvelOcallaghanIiiWithStreamedResponse

    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous JamesBurvelOcallaghanIii client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `JAMES_BURVEL_OCALLAGHAN_III_API_KEY`
        - `bearer_token` from `JAMES_BURVEL_OCALLAGHAN_III_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("JAMES_BURVEL_OCALLAGHAN_III_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("JAMES_BURVEL_OCALLAGHAN_III_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("JAMES_BURVEL_OCALLAGHAN_III_BASE_URL")
        if base_url is None:
            base_url = f"https://virtserver.swaggerhub.com/JOCALL3_1/jamesburvelocallaghaniiiapi/1.0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.users = users.UsersResource(self)
        self.accounts = accounts.AccountsResource(self)
        self.transactions = transactions.TransactionsResource(self)
        self.budgets = budgets.BudgetsResource(self)
        self.investments = investments.InvestmentsResource(self)
        self.ai = ai.AIResource(self)
        self.corporate = corporate.CorporateResource(self)
        self.web3 = web3.Web3Resource(self)
        self.payments = payments.PaymentsResource(self)
        self.sustainability = sustainability.SustainabilityResource(self)
        self.lending = lending.LendingResource(self)
        self.developers = developers.DevelopersResource(self)
        self.identity = identity.IdentityResource(self)
        self.goals = goals.GoalsResource(self)
        self.marketplace = marketplace.MarketplaceResource(self)
        self.with_raw_response = JamesBurvelOcallaghanIiiWithRawResponse(self)
        self.with_streaming_response = JamesBurvelOcallaghanIiiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._biometric_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _biometric_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.bearer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncJamesBurvelOcallaghanIii(AsyncAPIClient):
    users: users.AsyncUsersResource
    accounts: accounts.AsyncAccountsResource
    transactions: transactions.AsyncTransactionsResource
    budgets: budgets.AsyncBudgetsResource
    investments: investments.AsyncInvestmentsResource
    ai: ai.AsyncAIResource
    corporate: corporate.AsyncCorporateResource
    web3: web3.AsyncWeb3Resource
    payments: payments.AsyncPaymentsResource
    sustainability: sustainability.AsyncSustainabilityResource
    lending: lending.AsyncLendingResource
    developers: developers.AsyncDevelopersResource
    identity: identity.AsyncIdentityResource
    goals: goals.AsyncGoalsResource
    marketplace: marketplace.AsyncMarketplaceResource
    with_raw_response: AsyncJamesBurvelOcallaghanIiiWithRawResponse
    with_streaming_response: AsyncJamesBurvelOcallaghanIiiWithStreamedResponse

    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncJamesBurvelOcallaghanIii client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `JAMES_BURVEL_OCALLAGHAN_III_API_KEY`
        - `bearer_token` from `JAMES_BURVEL_OCALLAGHAN_III_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("JAMES_BURVEL_OCALLAGHAN_III_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("JAMES_BURVEL_OCALLAGHAN_III_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("JAMES_BURVEL_OCALLAGHAN_III_BASE_URL")
        if base_url is None:
            base_url = f"https://virtserver.swaggerhub.com/JOCALL3_1/jamesburvelocallaghaniiiapi/1.0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.users = users.AsyncUsersResource(self)
        self.accounts = accounts.AsyncAccountsResource(self)
        self.transactions = transactions.AsyncTransactionsResource(self)
        self.budgets = budgets.AsyncBudgetsResource(self)
        self.investments = investments.AsyncInvestmentsResource(self)
        self.ai = ai.AsyncAIResource(self)
        self.corporate = corporate.AsyncCorporateResource(self)
        self.web3 = web3.AsyncWeb3Resource(self)
        self.payments = payments.AsyncPaymentsResource(self)
        self.sustainability = sustainability.AsyncSustainabilityResource(self)
        self.lending = lending.AsyncLendingResource(self)
        self.developers = developers.AsyncDevelopersResource(self)
        self.identity = identity.AsyncIdentityResource(self)
        self.goals = goals.AsyncGoalsResource(self)
        self.marketplace = marketplace.AsyncMarketplaceResource(self)
        self.with_raw_response = AsyncJamesBurvelOcallaghanIiiWithRawResponse(self)
        self.with_streaming_response = AsyncJamesBurvelOcallaghanIiiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._biometric_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _biometric_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.bearer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class JamesBurvelOcallaghanIiiWithRawResponse:
    def __init__(self, client: JamesBurvelOcallaghanIii) -> None:
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.transactions = transactions.TransactionsResourceWithRawResponse(client.transactions)
        self.budgets = budgets.BudgetsResourceWithRawResponse(client.budgets)
        self.investments = investments.InvestmentsResourceWithRawResponse(client.investments)
        self.ai = ai.AIResourceWithRawResponse(client.ai)
        self.corporate = corporate.CorporateResourceWithRawResponse(client.corporate)
        self.web3 = web3.Web3ResourceWithRawResponse(client.web3)
        self.payments = payments.PaymentsResourceWithRawResponse(client.payments)
        self.sustainability = sustainability.SustainabilityResourceWithRawResponse(client.sustainability)
        self.lending = lending.LendingResourceWithRawResponse(client.lending)
        self.developers = developers.DevelopersResourceWithRawResponse(client.developers)
        self.identity = identity.IdentityResourceWithRawResponse(client.identity)
        self.goals = goals.GoalsResourceWithRawResponse(client.goals)
        self.marketplace = marketplace.MarketplaceResourceWithRawResponse(client.marketplace)


class AsyncJamesBurvelOcallaghanIiiWithRawResponse:
    def __init__(self, client: AsyncJamesBurvelOcallaghanIii) -> None:
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.transactions = transactions.AsyncTransactionsResourceWithRawResponse(client.transactions)
        self.budgets = budgets.AsyncBudgetsResourceWithRawResponse(client.budgets)
        self.investments = investments.AsyncInvestmentsResourceWithRawResponse(client.investments)
        self.ai = ai.AsyncAIResourceWithRawResponse(client.ai)
        self.corporate = corporate.AsyncCorporateResourceWithRawResponse(client.corporate)
        self.web3 = web3.AsyncWeb3ResourceWithRawResponse(client.web3)
        self.payments = payments.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.sustainability = sustainability.AsyncSustainabilityResourceWithRawResponse(client.sustainability)
        self.lending = lending.AsyncLendingResourceWithRawResponse(client.lending)
        self.developers = developers.AsyncDevelopersResourceWithRawResponse(client.developers)
        self.identity = identity.AsyncIdentityResourceWithRawResponse(client.identity)
        self.goals = goals.AsyncGoalsResourceWithRawResponse(client.goals)
        self.marketplace = marketplace.AsyncMarketplaceResourceWithRawResponse(client.marketplace)


class JamesBurvelOcallaghanIiiWithStreamedResponse:
    def __init__(self, client: JamesBurvelOcallaghanIii) -> None:
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.transactions = transactions.TransactionsResourceWithStreamingResponse(client.transactions)
        self.budgets = budgets.BudgetsResourceWithStreamingResponse(client.budgets)
        self.investments = investments.InvestmentsResourceWithStreamingResponse(client.investments)
        self.ai = ai.AIResourceWithStreamingResponse(client.ai)
        self.corporate = corporate.CorporateResourceWithStreamingResponse(client.corporate)
        self.web3 = web3.Web3ResourceWithStreamingResponse(client.web3)
        self.payments = payments.PaymentsResourceWithStreamingResponse(client.payments)
        self.sustainability = sustainability.SustainabilityResourceWithStreamingResponse(client.sustainability)
        self.lending = lending.LendingResourceWithStreamingResponse(client.lending)
        self.developers = developers.DevelopersResourceWithStreamingResponse(client.developers)
        self.identity = identity.IdentityResourceWithStreamingResponse(client.identity)
        self.goals = goals.GoalsResourceWithStreamingResponse(client.goals)
        self.marketplace = marketplace.MarketplaceResourceWithStreamingResponse(client.marketplace)


class AsyncJamesBurvelOcallaghanIiiWithStreamedResponse:
    def __init__(self, client: AsyncJamesBurvelOcallaghanIii) -> None:
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.transactions = transactions.AsyncTransactionsResourceWithStreamingResponse(client.transactions)
        self.budgets = budgets.AsyncBudgetsResourceWithStreamingResponse(client.budgets)
        self.investments = investments.AsyncInvestmentsResourceWithStreamingResponse(client.investments)
        self.ai = ai.AsyncAIResourceWithStreamingResponse(client.ai)
        self.corporate = corporate.AsyncCorporateResourceWithStreamingResponse(client.corporate)
        self.web3 = web3.AsyncWeb3ResourceWithStreamingResponse(client.web3)
        self.payments = payments.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.sustainability = sustainability.AsyncSustainabilityResourceWithStreamingResponse(client.sustainability)
        self.lending = lending.AsyncLendingResourceWithStreamingResponse(client.lending)
        self.developers = developers.AsyncDevelopersResourceWithStreamingResponse(client.developers)
        self.identity = identity.AsyncIdentityResourceWithStreamingResponse(client.identity)
        self.goals = goals.AsyncGoalsResourceWithStreamingResponse(client.goals)
        self.marketplace = marketplace.AsyncMarketplaceResourceWithStreamingResponse(client.marketplace)


Client = JamesBurvelOcallaghanIii

AsyncClient = AsyncJamesBurvelOcallaghanIii
