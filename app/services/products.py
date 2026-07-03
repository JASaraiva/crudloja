from sqlalchemy.orm import Session
from app import repository, models, schemas

class ProductService:

    def create_product(self, db: Session, product: schemas.ProductCreate) -> models.Product:
        return repository.create_product(db, product)
    
    def get_product(self, db: Session, product_id: int) -> models.Product:
        return repository.get_product(db, product_id)

    def list_products(self, db: Session) -> list[models.Product]:
        return repository.list_products(db)

    def update_product(self, db: Session, product_id: int, product_data: schemas.ProductCreate) -> models.Product:
        return repository.update_product(db, product_id, product_data)

    def delete_product(self, db: Session, product_id: int) -> models.Product:
        return repository.delete_product(db, product_id)
        