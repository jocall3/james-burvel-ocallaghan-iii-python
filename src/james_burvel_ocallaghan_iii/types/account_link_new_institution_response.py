# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountLinkNewInstitutionResponse"]


class AccountLinkNewInstitutionResponse(BaseModel):
    auth_uri: object = FieldInfo(alias="authUri")
    """
    The URI to redirect the user to complete authentication with the external
    institution.
    """

    link_session_id: object = FieldInfo(alias="linkSessionId")
    """Unique session ID for the account linking process."""

    status: Literal["pending_user_action", "completed", "failed"]
    """Current status of the linking process."""

    message: Optional[object] = None
    """A descriptive message regarding the next steps."""
