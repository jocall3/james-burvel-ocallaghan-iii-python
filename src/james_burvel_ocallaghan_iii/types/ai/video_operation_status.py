# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VideoOperationStatus"]


class VideoOperationStatus(BaseModel):
    message: str
    """A descriptive message about the current stage or any issues."""

    operation_id: str = FieldInfo(alias="operationId")
    """Unique identifier for the video generation operation."""

    progress_percentage: int = FieldInfo(alias="progressPercentage")
    """Progress of the operation in percentage."""

    status: Literal["queued", "generating", "rendering", "done", "error"]
    """Current status of the video generation."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Timestamp when the video generation was completed or failed."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the video generation request was created."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Detailed error message if the status is 'error'."""

    preview_image_uri: Optional[str] = FieldInfo(alias="previewImageUri", default=None)
    """Temporary, signed URL to a preview image/thumbnail of the video."""

    video_uri: Optional[str] = FieldInfo(alias="videoUri", default=None)
    """
    Temporary, signed URL to the generated video asset (available when status is
    'done').
    """
