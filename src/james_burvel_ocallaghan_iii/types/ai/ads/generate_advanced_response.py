# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["GenerateAdvancedResponse"]


class GenerateAdvancedResponse(BaseModel):
    estimated_completion_time_seconds: Optional[int] = FieldInfo(alias="estimatedCompletionTimeSeconds", default=None)
    """Estimated time until advanced video generation is complete.

    May be longer than standard generation.
    """

    operation_id: Optional[str] = FieldInfo(alias="operationId", default=None)
    """The unique identifier for the advanced video generation operation."""
