from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate
from fastapi import HTTPException, status


class CategoryRepository:

    def create_category(self, db: Session, category: CategoryCreate) -> Category:
        db_category = Category(**category.model_dump())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    def get_category(self, db: Session, category_id: int) -> Category:
        stmt = select(Category).where(Category.id == category_id)
        category = db.execute(stmt).scalar_one_or_none()

        if category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

        return category

    def list_categories(self, db: Session) -> list[Category]:
        stmt = select(Category)
        return db.execute(stmt).scalars().all()

    def update_category(self, db: Session, category_id: int, category_data: CategoryUpdate) -> Category:
        category = self.get_category(db, category_id)

        for key, value in category_data.model_dump().items():
            setattr(category, key, value)
        db.commit()
        db.refresh(category)
        return category

    def delete_category(self, db: Session, category_id: int) -> None:
        category = self.get_category(db, category_id)

        db.delete(category)
        db.commit()