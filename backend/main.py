from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime


from auth import create_access_token
from tools.expence_tools import add_expense_tool
from auth import verify_password
from auth import get_current_user



import model
import schemas
import crud

from database import engine, get_db

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Budget Tracker API Running"}


@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):

    created_user = crud.create_user(
        db,
        user.email,
        user.password
    )

    return {
        "message": "User created",
        "email": created_user.email
    }


@app.post("/expense")
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    created_expense = crud.create_expense(
        db,
        expense.amount,
        expense.category,
        expense.merchant,
        user_id=1
    )

    return created_expense





@app.post("/budget")
def add_budget(
    budget: schemas.BudgetCreate,
    db: Session = Depends(get_db)
):

    created_budget = crud.create_budget(
        db,
        budget.category,
        budget.monthly_limit,
        user_id=1
    )

    return created_budget


@app.get("/expenses")
def get_expenses(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    expenses = (
        db.query(model.Expense)
        .filter(
            model.Expense.user_id
            == current_user["user_id"]
        )
        .all()
    )

    return expenses
    
@app.post("/chat")
def chat(
    message: schemas.ChatRequest
):

    return {
        "message":
        "Use ADK Web UI for now.",
        "user_message":
        message.message
    }

@app.post("/login")
def login(
    user: schemas.LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = crud.get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token({
        "user_id": db_user.id
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }




