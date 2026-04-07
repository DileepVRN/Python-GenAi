from pydantic import BaseModel

class TransferRequest(BaseModel):
    from_account: int
    to_account: int
    amount: float