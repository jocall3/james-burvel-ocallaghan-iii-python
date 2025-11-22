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
    """Country of residence or operation (ISO 3166-1 alpha-2 code)."""

    entity_type: Required[Annotated[Literal["individual", "organization"], PropertyInfo(alias="entityType")]]
    """The type of entity being screened."""

    name: Required[str]
    """Full name of the individual or organization to screen."""

    address: Optional[AddressParam]
    """Full address for enhanced screening."""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]
    """Date of birth for individual screening (YYYY-MM-DD)."""
