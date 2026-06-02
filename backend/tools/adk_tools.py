from database import SessionLocal

from tools.expence_tools import add_expense_tool
from tools.budget_tools import create_budget_tool
from tools.summary_tools import get_budget_summary_tool
from tools.analytics_tools import get_spending_analysis_tool


def add_expense(
    amount: float,
    category: str,
    merchant: str
):
    db = SessionLocal()

    try:
        return add_expense_tool(
            db=db,
            amount=amount,
            category=category,
            merchant=merchant
        )

    finally:
        db.close()


def create_budget(
    category: str,
    monthly_limit: float
):
    db = SessionLocal()

    try:
        return create_budget_tool(
            db=db,
            category=category,
            monthly_limit=monthly_limit
        )

    finally:
        db.close()


def get_budget_summary():
    db = SessionLocal()

    try:
        return get_budget_summary_tool(db)

    finally:
        db.close()


def spending_analysis():
    db = SessionLocal()

    try:
        return get_spending_analysis_tool(db)

    finally:
        db.close()