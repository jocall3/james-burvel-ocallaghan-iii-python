# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .address_param import AddressParam

__all__ = ["CorporatePerformSanctionScreeningParams"]


class CorporatePerformSanctionScreeningParams(TypedDict, total=False):
    country: Required[object]
    """
    Two-letter ISO country code related to the entity (e.g., country of residence,
    registration).
    """

    entity_type: Required[Annotated[Literal["individual", "organization"], PropertyInfo(alias="entityType")]]
    """The type of entity being screened."""

    name: Required[object]
    """Full name of the individual or organization to screen."""

    address: AddressParam

    date_of_birth: Annotated[object, PropertyInfo(alias="dateOfBirth")]
    """Date of birth for individuals (YYYY-MM-DD)."""

    identification_number: Annotated[object, PropertyInfo(alias="identificationNumber")]
    """
    Optional: Any government-issued identification number (e.g., passport, national
    ID).
    """
