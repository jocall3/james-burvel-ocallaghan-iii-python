# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["KYCSubmitParams"]


class KYCSubmitParams(TypedDict, total=False):
    country_of_issue: Required[Annotated[str, PropertyInfo(alias="countryOfIssue")]]
    """The country that issued the document (ISO 3166-1 alpha-2)."""

    document_front_image: Required[
        Annotated[Union[str, Base64FileInput], PropertyInfo(alias="documentFrontImage", format="base64")]
    ]
    """Base64 encoded image of the front side of the document."""

    document_number: Required[Annotated[str, PropertyInfo(alias="documentNumber")]]
    """The unique identifier number from the document."""

    document_type: Required[
        Annotated[
            Literal["drivers_license", "passport", "national_id", "utility_bill", "bank_statement"],
            PropertyInfo(alias="documentType"),
        ]
    ]
    """Type of KYC document being submitted."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]]
    """The date the document expires."""

    issue_date: Required[Annotated[Union[str, date], PropertyInfo(alias="issueDate", format="iso8601")]]
    """The date the document was issued."""

    additional_notes: Annotated[Optional[str], PropertyInfo(alias="additionalNotes")]
    """Any additional notes or comments for the KYC review team."""

    address_proof_image: Annotated[
        Union[str, Base64FileInput, None], PropertyInfo(alias="addressProofImage", format="base64")
    ]
    """Base64 encoded image of an address proof document (e.g., utility bill)."""

    document_back_image: Annotated[
        Union[str, Base64FileInput, None], PropertyInfo(alias="documentBackImage", format="base64")
    ]
    """Base64 encoded image of the back side of the document (if applicable)."""
