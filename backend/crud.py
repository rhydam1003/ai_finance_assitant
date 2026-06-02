from sqlalchemy.orm import Session
from model import User, Expense ,Budget
from auth import hash_password


def create_user(db: Session, email: str, password: str):
    user = User(
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user



def create_expense(db: Session, amount, category, merchant, user_id):
    expense = Expense(
        amount=amount,
        category=category,
        merchant=merchant,
        user_id=user_id
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense






def create_budget(
    db,
    category,
    monthly_limit,
    user_id
):
    budget = Budget(
        category=category,
        monthly_limit=monthly_limit,
        user_id=user_id
    )

    db.add(budget)
    db.commit()
    db.refresh(budget)

    return budget

def get_user_by_email(db, email):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )