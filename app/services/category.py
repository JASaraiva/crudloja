from app.repositories import CategoryRepository
from app.exceptions import CategoryNotFoundException
from app.models import Category
from app.schemas import CategoryCreate


class CategoryService():
    
    def __init__(self, repository: CategoryRepository):
        self.repository = repository


    def get(self, category_id: int) -> Category:

        category = self.repository.get(category_id)

        if category is None:
            raise CategoryNotFoundException(category_id)
        
        return category
    

    
    def list(self) -> Category:
        categories = self.repository.list()
        return categories
    

    def create(self, category_data: CategoryCreate) -> Category: 
        return self.repository.create(category_data)
        
