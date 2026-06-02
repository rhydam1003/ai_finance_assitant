from sqlalchemy import func
import model


def get_budget_summary_tool(db):

    budgets = db.query(model.Budget).all()

    result = []

    for budget in budgets:

        spent = (
            db.query(func.sum(model.Expense.amount))
            .filter(
                model.Expense.category == budget.category
            )
            .scalar()
        )

        spent = spent or 0

        remaining = budget.monthly_limit - spent

        result.append({
            "category": budget.category,
            "budget": budget.monthly_limit,
            "spent": spent,
            "remaining": remaining
        })

    return result