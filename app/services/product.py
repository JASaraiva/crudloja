from app.repositories import ProductRepository

class ProductService(ProductRepository):
    pass
        


def get_product_service() -> ProductService:
    return ProductService(repository=ProductRepository())