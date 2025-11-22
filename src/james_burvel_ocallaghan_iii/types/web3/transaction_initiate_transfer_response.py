# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransactionInitiateTransferResponse"]


class TransactionInitiateTransferResponse(BaseModel):
    status: Literal["pending_signature", "broadcasting", "confirmed", "failed"]
    """Current status of the crypto transfer."""

    transfer_id: str = FieldInfo(alias="transferId")
    """Unique identifier for the initiated crypto transfer."""

    blockchain_txn_hash: Optional[str] = FieldInfo(alias="blockchainTxnHash", default=None)
    """The transaction hash on the blockchain once broadcasted."""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when the status was last updated."""

    message: Optional[str] = None
    """A descriptive message about the current status or required action."""
