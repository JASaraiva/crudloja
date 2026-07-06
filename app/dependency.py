from app.services import ProductService, CategoryService

def get_product_service() -> ProductService:
    return ProductService()

def get_category_service() -> CategoryService:
    return CategoryService()