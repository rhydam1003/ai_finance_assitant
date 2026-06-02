from model import Budget


def create_budget_tool(
    db,
    category,
    monthly_limit,
    user_id=1
):

    existing_budget = (
        db.query(Budget)
        .filter(
            Budget.category == category,
            Budget.user_id == user_id
        )
        .first()
    )

    # UPDATE existing budget
    if existing_budget:

        existing_budget.monthly_limit = monthly_limit

        db.commit()

        return {
            "message": "Budget updated",
            "budget_id": existing_budget.id
        }

    # CREATE new budget
    budget = Budget(
        category=category,
        monthly_limit=monthly_limit,
        user_id=user_id
    )

    db.add(budget)
    db.commit()
    db.refresh(budget)

    return {
        "message": "Budget created",
        "budget_id": budget.id
    }