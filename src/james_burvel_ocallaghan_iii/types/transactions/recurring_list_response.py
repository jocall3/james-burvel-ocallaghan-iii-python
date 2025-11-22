# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .recurring_transaction import RecurringTransaction

__all__ = ["RecurringListResponse"]

RecurringListResponse: TypeAlias = List[RecurringTransaction]
