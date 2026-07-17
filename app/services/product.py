from app.repositories import ProductRepository
from app.exceptions import ProductNotFoundException
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate


class ProductService():

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get(self, product_id: int) -> Product:
        product = self.repository.get(product_id)
        if product is None:
            raise ProductNotFoundException()
        return product

    def list(self) -> list[Product]:
        return self.repository.list()

    def create(self, product_data: ProductCreate) -> Product:
        return self.repository.create(product_data)

    def update(self, product_id: int, product_data: ProductUpdate) -> Product:
        updated = self.repository.update(product_id, product_data)
        if updated is None:
            raise ProductNotFoundException()
        return updated

    def delete(self, product_id: int) -> None:
        self.get(product_id)
        self.repository.delete(product_id)
