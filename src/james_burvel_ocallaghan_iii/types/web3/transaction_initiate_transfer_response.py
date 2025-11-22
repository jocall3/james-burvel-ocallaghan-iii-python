# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransactionInitiateTransferResponse"]


class TransactionInitiateTransferResponse(BaseModel):
    status: Literal["pending_signature", "pending_broadcast", "in_progress", "completed", "failed", "cancelled"]
    """Current status of the cryptocurrency transfer."""

    transfer_id: str = FieldInfo(alias="transferId")
    """Unique identifier for the initiated transfer."""

    blockchain_txn_hash: Optional[str] = FieldInfo(alias="blockchainTxnHash", default=None)
    """The transaction hash on the blockchain (if available)."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Timestamp when the transfer was completed (if successful)."""

    message: Optional[str] = None
    """A descriptive message regarding the transfer status or next steps."""
