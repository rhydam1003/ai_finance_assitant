from sqlalchemy.orm import Session
from model import Expense


def add_expense_tool(
    db,
    amount,
    category,
    merchant,
    user_id=1
):

    expense = Expense(
        amount=amount,
        category=category,
        merchant=merchant,
        user_id=user_id
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return {
        "message": "Expense added successfully",
        "expense_id": expense.id
    }