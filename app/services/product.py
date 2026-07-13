from app.repositories import ProductRepository
from app.exceptions import ProductNotFoundException
from app.models import Product
from app.schemas import ProductCreate


class ProductService():
    
    def __init__(self, repository: ProductRepository):
        self.repository = repository


    def get_product(self, product_id: int) -> Product:

        product = self.repository.get_product(product_id)

        if product is None:
            raise ProductNotFoundException(product_id)
        
        return product
    

    
    def list_products(self) -> Product:
        products = self.repository.list_products()
        return products
    

    def create_product(self, product_data: ProductCreate) -> Product: 
        return self.repository.create_product(product_data)
        
