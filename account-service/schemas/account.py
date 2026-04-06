from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    balance: float

class AccountResponse(AccountCreate):
    id: int

    class Config:
        orm_mode = True