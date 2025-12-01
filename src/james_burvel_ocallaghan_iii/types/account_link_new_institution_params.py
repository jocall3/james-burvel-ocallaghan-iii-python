# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountLinkNewInstitutionParams"]


class AccountLinkNewInstitutionParams(TypedDict, total=False):
    country_code: Required[Annotated[object, PropertyInfo(alias="countryCode")]]
    """Two-letter ISO country code of the institution."""

    institution_name: Required[Annotated[object, PropertyInfo(alias="institutionName")]]
    """Name of the financial institution to link."""

    provider_identifier: Annotated[object, PropertyInfo(alias="providerIdentifier")]
    """
    Optional: Specific identifier for a third-party linking provider (e.g., 'plaid',
    'finicity').
    """

    redirect_uri: Annotated[object, PropertyInfo(alias="redirectUri")]
    """
    Optional: URI to redirect the user after completing the external authentication
    flow.
    """
