# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .address_param import AddressParam

__all__ = ["CorporatePerformSanctionScreeningParams"]


class CorporatePerformSanctionScreeningParams(TypedDict, total=False):
    country: Required[str]
    """The primary country of residence or operation (ISO 3166-1 alpha-2)."""

    entity_type: Required[Annotated[Literal["individual", "organization"], PropertyInfo(alias="entityType")]]
    """The type of entity being screened."""

    name: Required[str]
    """The full name of the individual or organization to screen."""

    address: Optional[AddressParam]
    """Optional: Address details for improved screening."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]
    """Optional: Date of birth for individuals, for better match accuracy."""

    id_number: Annotated[Optional[str], PropertyInfo(alias="idNumber")]
    """Optional: Government-issued ID number for individuals."""
