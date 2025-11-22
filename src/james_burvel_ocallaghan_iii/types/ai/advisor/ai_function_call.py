# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AIFunctionCall"]


class AIFunctionCall(BaseModel):
    id: str
    """A unique identifier for this specific function call instance."""

    args: object
    """The arguments to pass to the tool/function, as a JSON object."""

    name: str
    """The name of the tool/function to call."""

    description: Optional[str] = None
    """
    A natural language explanation of why the AI wants to call this function, for
    user confirmation.
    """
