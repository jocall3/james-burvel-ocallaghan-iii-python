# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountLinkNewInstitutionParams"]


class AccountLinkNewInstitutionParams(TypedDict, total=False):
    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """Two-letter ISO country code of the institution."""

    institution_name: Required[Annotated[str, PropertyInfo(alias="institutionName")]]
    """Name of the financial institution to link."""

    provider_identifier: Annotated[Optional[str], PropertyInfo(alias="providerIdentifier")]
    """
    Optional: Specific identifier for a third-party linking provider (e.g., 'plaid',
    'finicity').
    """

    redirect_uri: Annotated[Optional[str], PropertyInfo(alias="redirectUri")]
    """
    Optional: URI to redirect the user after completing the external authentication
    flow.
    """
