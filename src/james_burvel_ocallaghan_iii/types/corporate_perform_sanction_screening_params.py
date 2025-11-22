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
    """ISO 3166-1 alpha-2 country code relevant to the individual/entity."""

    entity_type: Required[Annotated[Literal["individual", "organization"], PropertyInfo(alias="entityType")]]
    """Type of entity being screened."""

    name: Required[str]
    """The full name of the individual or entity to screen."""

    address: Optional[AddressParam]
    """Optional: Address details for enhanced screening accuracy."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]
    """Date of birth, if screening an individual."""

    identification_number: Annotated[Optional[str], PropertyInfo(alias="identificationNumber")]
    """Optional: Any identification number (e.g., passport, EIN)."""
