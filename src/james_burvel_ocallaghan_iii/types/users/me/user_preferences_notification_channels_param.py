# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserPreferencesNotificationChannelsParam"]


class UserPreferencesNotificationChannelsParam(TypedDict, total=False):
    email: object

    in_app: Annotated[object, PropertyInfo(alias="inApp")]

    push: object

    sms: object
