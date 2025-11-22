# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TransactionDisputeParams"]


class TransactionDisputeParams(TypedDict, total=False):
    details: Required[str]
    """Detailed explanation of the dispute."""

    reason: Required[
        Literal["unauthorized", "duplicate", "incorrect_amount", "service_not_received", "damaged_goods", "other"]
    ]
    """The primary reason for disputing the transaction."""

    supporting_documents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="supportingDocuments")]
    """Optional URLs to supporting documents (e.g., screenshots, photos)."""
