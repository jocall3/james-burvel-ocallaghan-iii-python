# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Web3RetrieveNFTsResponse", "Data", "DataAttribute"]


class DataAttribute(BaseModel):
    trait_type: Optional[object] = None

    value: Optional[object] = None


class Data(BaseModel):
    id: object
    """Unique identifier for the NFT within the system."""

    blockchain_network: object = FieldInfo(alias="blockchainNetwork")
    """Blockchain network on which the NFT exists."""

    collection_name: object = FieldInfo(alias="collectionName")
    """Name of the NFT collection."""

    contract_address: object = FieldInfo(alias="contractAddress")
    """Blockchain contract address of the NFT collection."""

    image_url: object = FieldInfo(alias="imageUrl")
    """URL to the NFT's image."""

    name: object
    """Name of the specific NFT."""

    owner_address: object = FieldInfo(alias="ownerAddress")
    """Blockchain address of the current owner."""

    token_id: object = FieldInfo(alias="tokenId")
    """Unique ID of the token within its contract."""

    attributes: Optional[List[DataAttribute]] = None
    """Key-value attributes of the NFT (e.g., rarity traits)."""

    description: Optional[object] = None
    """Description of the NFT."""

    estimated_value_usd: Optional[object] = FieldInfo(alias="estimatedValueUSD", default=None)
    """AI-estimated current market value in USD."""

    last_sale_price_usd: Optional[object] = FieldInfo(alias="lastSalePriceUSD", default=None)
    """Last known sale price in USD."""


class Web3RetrieveNFTsResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
