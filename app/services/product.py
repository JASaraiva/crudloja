from sqlalchemy.orm import Session
from app.schemas import ProductCreate
from app.models import Product
from app.repositories import product

class ProductService:

    def create_product(self, db: Session, product: ProductCreate) -> Product:
        return product.create_product(db, product)

    def get_product(self, db: Session, product_id: int) -> Product:
        return product.get_product(db, product_id)

    def list_products(self, db: Session) -> list[Product]:
        return product.list_products(db)

    def update_product(self, db: Session, product_id: int, product_data: ProductCreate) -> Product:
        return product.update_product(db, product_id, product_data)

    def delete_product(self, db: Session, product_id: int) -> Product:
        return product.delete_product(db, product_id)
        