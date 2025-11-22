# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountLinkNewInstitutionParams"]


class AccountLinkNewInstitutionParams(TypedDict, total=False):
    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3166-1 alpha-2 country code of the institution."""

    institution_name: Required[Annotated[str, PropertyInfo(alias="institutionName")]]
    """The name of the financial institution to link."""

    metadata: Optional[object]
    """Optional: Additional provider-specific metadata for linking."""

    provider_type: Annotated[Optional[Literal["plaid", "mx", "finicity", "other"]], PropertyInfo(alias="providerType")]
    """Optional: The type of third-party linking provider to use."""
