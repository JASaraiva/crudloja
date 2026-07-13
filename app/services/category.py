from app.repositories import CategoryRepository
from app.exceptions import CategoryNotFoundException
from app.models import Category
from app.schemas import CategoryCreate


class CategoryService():
    
    def __init__(self, repository: CategoryRepository):
        self.repository = repository


    def get_category(self, category_id: int) -> Category:

        category = self.repository.get_category(category_id)

        if category is None:
            raise CategoryNotFoundException(category_id)
        
        return category
    

    
    def list_categories(self) -> Category:
        categories = self.repository.list_categories()
        return categories
    

    def create_category(self, category_data: CategoryCreate) -> Category: 
        return self.repository.create_category(category_data)
        
