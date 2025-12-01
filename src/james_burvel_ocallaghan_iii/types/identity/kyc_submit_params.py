# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["KYCSubmitParams"]


class KYCSubmitParams(TypedDict, total=False):
    country_of_issue: Required[Annotated[str, PropertyInfo(alias="countryOfIssue")]]
    """The two-letter ISO country code where the document was issued."""

    document_number: Required[Annotated[str, PropertyInfo(alias="documentNumber")]]
    """The identification number on the document."""

    document_type: Required[
        Annotated[
            Literal["drivers_license", "passport", "national_id", "utility_bill", "bank_statement", "other"],
            PropertyInfo(alias="documentType"),
        ]
    ]
    """The type of KYC document being submitted."""

    expiration_date: Required[Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]]
    """The expiration date of the document (YYYY-MM-DD)."""

    issue_date: Required[Annotated[Union[str, date], PropertyInfo(alias="issueDate", format="iso8601")]]
    """The issue date of the document (YYYY-MM-DD)."""

    additional_documents: Annotated[
        Optional[SequenceNotStr[Union[str, Base64FileInput]]],
        PropertyInfo(alias="additionalDocuments", format="base64"),
    ]
    """Array of additional documents (e.g., utility bills) as base64 encoded images."""

    document_back_image: Annotated[
        Union[str, Base64FileInput, None], PropertyInfo(alias="documentBackImage", format="base64")
    ]
    """Base64 encoded image of the back of the document (if applicable)."""

    document_front_image: Annotated[
        Union[str, Base64FileInput, None], PropertyInfo(alias="documentFrontImage", format="base64")
    ]
    """Base64 encoded image of the front of the document.

    Use 'application/json' with base64 string, or 'multipart/form-data' for direct
    file upload.
    """
