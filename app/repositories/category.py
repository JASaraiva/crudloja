from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_category(self, category: CategoryCreate) -> Category:
        db_category = Category(**category.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category


    def get_category(self, category_id: int) -> Category | None:
        stmt = select(Category).where(Category.id == category_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list_categories(self) -> list[Category]:
        stmt = select(Category)
        return self.db.execute(stmt).scalars().all()


    def update_category(self, category_id: int, category_data: CategoryUpdate) -> Category:
        category = self.get_category(category_id)

        for key, value in category_data.model_dump().items():
            setattr(category, key, value)
        self.db.commit()
        self.db.refresh(category)
        return category


    def delete_category(self, category_id: int) -> None:
        category = self.get_category(category_id)
        self.db.delete(category)
        self.db.commit()
