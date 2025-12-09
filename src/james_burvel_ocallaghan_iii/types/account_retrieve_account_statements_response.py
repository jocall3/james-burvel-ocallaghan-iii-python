# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveAccountStatementsResponse", "DownloadURLs"]


class DownloadURLs(BaseModel):
    """Map of available download URLs for different formats."""

    csv: Optional[object] = None
    """Signed URL to download the statement in CSV format."""

    pdf: Optional[object] = None
    """Signed URL to download the statement in PDF format."""


class AccountRetrieveAccountStatementsResponse(BaseModel):
    account_id: object = FieldInfo(alias="accountId")
    """The account ID the statement belongs to."""

    download_urls: DownloadURLs = FieldInfo(alias="downloadUrls")
    """Map of available download URLs for different formats."""

    period: object
    """The period covered by the statement."""

    statement_id: object = FieldInfo(alias="statementId")
    """Unique identifier for the statement."""
