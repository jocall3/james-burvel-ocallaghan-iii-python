# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VideoOperationStatus"]


class VideoOperationStatus(BaseModel):
    message: str
    """A descriptive message about the current stage or status."""

    operation_id: str = FieldInfo(alias="operationId")
    """The unique identifier for the video generation operation."""

    progress_percentage: int = FieldInfo(alias="progressPercentage")
    """Current progress of the operation as a percentage."""

    status: Literal["queued", "processing", "rendering", "done", "error"]
    """Current status of the video generation job."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """If an error occurred, a message describing the error."""

    preview_image_uri: Optional[str] = FieldInfo(alias="previewImageUri", default=None)
    """URL to a preview image/thumbnail of the video."""

    video_uri: Optional[str] = FieldInfo(alias="videoUri", default=None)
    """URL to the final generated video asset (available when status is 'done')."""
