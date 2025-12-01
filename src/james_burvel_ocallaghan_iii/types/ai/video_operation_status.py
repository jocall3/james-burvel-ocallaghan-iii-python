# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VideoOperationStatus"]


class VideoOperationStatus(BaseModel):
    message: str
    """A descriptive status message."""

    operation_id: str = FieldInfo(alias="operationId")
    """The unique identifier for the video generation operation."""

    progress_percentage: int = FieldInfo(alias="progressPercentage")
    """Estimated completion percentage (0-100)."""

    status: Literal["queued", "generating", "rendering", "done", "error"]
    """Current status of the video generation job."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error message if the operation failed."""

    preview_image_uri: Optional[str] = FieldInfo(alias="previewImageUri", default=None)
    """Temporary, signed URL to a preview image/thumbnail of the video."""

    video_uri: Optional[str] = FieldInfo(alias="videoUri", default=None)
    """
    Temporary, signed URL to the generated video asset (available when status is
    'done').
    """
