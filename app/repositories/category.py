from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas import  CategoryCreate, CategoryUpdate, CategoryResponse
from fastapi import HTTPException, status


def create_category(db: Session, category: CategoryCreate) -> CategoryResponse:
    category = CategoryResponse(**category.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category(db: Session, category_id: int) -> CategoryResponse:
    stmt = select(CategoryResponse).where(CategoryResponse.id == category_id)
    category = db.execute(stmt).scalar_one_or_none()

    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return category

def list_categories(db: Session) -> list[CategoryResponse]:
    stmt = select(CategoryResponse)
    return db.execute(stmt).scalars().all()

def update_category(db: Session, category_id: int, category_data: CategoryCreate) -> CategoryResponse:
    category = get_category(db, category_id)

    for key, value in category_data.model_dump().items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int) -> CategoryResponse:
    category = get_category(db, category_id)

    db.delete(category)
    db.commit()
    return category