# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveAccountStatementsResponse", "DownloadURLs"]


class DownloadURLs(BaseModel):
    csv: Optional[str] = None
    """Signed URL to download the statement in CSV format."""

    pdf: Optional[str] = None
    """Signed URL to download the statement in PDF format."""


class AccountRetrieveAccountStatementsResponse(BaseModel):
    account_id: str = FieldInfo(alias="accountId")
    """The account ID the statement belongs to."""

    download_urls: DownloadURLs = FieldInfo(alias="downloadUrls")
    """Map of available download URLs for different formats."""

    period: str
    """The period covered by the statement."""

    statement_id: str = FieldInfo(alias="statementId")
    """Unique identifier for the statement."""
