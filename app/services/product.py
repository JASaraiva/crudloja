from app.repositories import ProductRepository
from app.exceptions import ProductNotFoundException
from app.models import Product

class ProductService():
    
    def __init__(self, repository: ProductRepository):
        self.repository = repository


    def get(self, product_id: int) -> Product:

        product = self.repository.get_product(product_id)

        if product is None:
            raise ProductNotFoundException(product_id)
        
        return product
    

    
    def list(self) -> Product:
        products = self.repository.list()
        return products
    

    def create(self, product_create: Product) -> Product: 
        db_product = Product(**product_create.model_dump())

        return self.repository.create(db_product)
        
