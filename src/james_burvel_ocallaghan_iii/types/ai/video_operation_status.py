# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VideoOperationStatus"]


class VideoOperationStatus(BaseModel):
    message: str
    """A descriptive message about the current progress or status."""

    operation_id: str = FieldInfo(alias="operationId")
    """Unique identifier for the video generation operation."""

    progress_percentage: int = FieldInfo(alias="progressPercentage")
    """Percentage completion of the video generation."""

    status: Literal["queued", "generating", "rendering", "done", "error"]
    """Current status of the video generation job."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """If status is 'error', provides details about why the generation failed."""

    generated_at: Optional[datetime] = FieldInfo(alias="generatedAt", default=None)
    """Timestamp when the video was successfully generated."""

    preview_image_uri: Optional[str] = FieldInfo(alias="previewImageUri", default=None)
    """URL to a static preview image/thumbnail of the video."""

    video_uri: Optional[str] = FieldInfo(alias="videoUri", default=None)
    """
    Temporary, signed URL to the generated video asset (available when status is
    'done').
    """
