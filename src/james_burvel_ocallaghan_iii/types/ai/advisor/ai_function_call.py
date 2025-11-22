# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["AIFunctionCall"]


class AIFunctionCall(BaseModel):
    id: str
    """Unique identifier for this specific function call."""

    args: object
    """A JSON object containing the arguments for the function call."""

    name: str
    """The name of the tool function to be called."""
