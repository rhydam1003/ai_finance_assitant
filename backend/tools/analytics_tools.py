from sqlalchemy import func
import model


def get_spending_analysis_tool(db):

    expenses = db.query(model.Expense).all()

    total_spent = (
        db.query(
            func.sum(model.Expense.amount)
        )
        .scalar()
    )

    category_data = (
        db.query(
            model.Expense.category,
            func.sum(model.Expense.amount)
        )
        .group_by(model.Expense.category)
        .all()
    )

    categories = []

    highest_category = None
    highest_amount = 0

    for category, amount in category_data:

        categories.append({
            "category": category,
            "amount": amount
        })

        if amount > highest_amount:

            highest_amount = amount
            highest_category = category

    return {
        "total_spent": total_spent or 0,
        "top_category": highest_category,
        "top_category_amount": highest_amount,
        "categories": categories
    }