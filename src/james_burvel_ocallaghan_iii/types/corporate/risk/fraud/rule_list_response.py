# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .fraud_rule import FraudRule

__all__ = ["RuleListResponse"]

RuleListResponse: TypeAlias = List[FraudRule]
