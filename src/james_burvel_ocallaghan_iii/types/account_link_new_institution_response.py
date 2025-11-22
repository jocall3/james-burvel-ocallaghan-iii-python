# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountLinkNewInstitutionResponse"]


class AccountLinkNewInstitutionResponse(BaseModel):
    auth_uri: str = FieldInfo(alias="authUri")
    """
    The URI to which the user should be redirected to complete the authentication
    process with the external institution.
    """

    link_session_id: str = FieldInfo(alias="linkSessionId")
    """A unique identifier for the account linking session."""

    status: Literal["pending_user_action", "error"]
    """Current status of the linking process."""

    message: Optional[str] = None
    """A descriptive message about the next steps or any errors."""
