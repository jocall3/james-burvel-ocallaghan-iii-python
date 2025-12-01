# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserPreferencesNotificationChannels"]


class UserPreferencesNotificationChannels(BaseModel):
    email: Optional[object] = None

    in_app: Optional[object] = FieldInfo(alias="inApp", default=None)

    push: Optional[object] = None

    sms: Optional[object] = None
