# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .investment_portfolio import InvestmentPortfolio

__all__ = ["PortfolioListResponse"]

PortfolioListResponse: TypeAlias = List[InvestmentPortfolio]
