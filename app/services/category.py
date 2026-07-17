from app.repositories import CategoryRepository
from app.exceptions import CategoryNotFoundException
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate


class CategoryService():

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def get(self, category_id: int) -> Category:
        category = self.repository.get(category_id)
        if category is None:
            raise CategoryNotFoundException()
        return category

    def list(self) -> list[Category]:
        return self.repository.list()

    def create(self, category_data: CategoryCreate) -> Category:
        return self.repository.create(category_data)

    def update(self, category_id: int, category_data: CategoryUpdate) -> Category:
        updated = self.repository.update(category_id, category_data)
        if updated is None:
            raise CategoryNotFoundException()
        return updated

    def delete(self, category_id: int) -> None:
        self.get(category_id)
        self.repository.delete(category_id)
