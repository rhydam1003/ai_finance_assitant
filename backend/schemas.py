from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    merchant: Optional[str] = None


class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    merchant: Optional[str]

    class Config:
        from_attributes = True


class BudgetCreate(BaseModel):
    category: str
    monthly_limit: float


class BudgetResponse(BaseModel):
    id: int
    category: str
    monthly_limit: float

    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    message: str


class LoginRequest(BaseModel):
    email: str
    password: str