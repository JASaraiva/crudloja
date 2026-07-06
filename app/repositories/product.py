from sqlalchemy.orm import Session
from sqlalchemy import select
from app.repositories import CategoryRepository
from app.schemas import ProductCreate, ProductUpdate
from app.models import Product
from fastapi import HTTPException, status


class ProductRepository:

    def create_product(self, db: Session, product: ProductCreate) -> Product:
        CategoryRepository().get_category(db, product.category_id)

        db_product = Product(**product.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def get_product(self, db: Session, product_id: int) -> Product:
        stmt = select(Product).where(Product.id == product_id)
        product = db.execute(stmt).scalar_one_or_none()

        if product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        return product

    def list_products(self, db: Session) -> list[Product]:
        stmt = select(Product)
        return db.execute(stmt).scalars().all()

    def update_product(self, db: Session, product_id: int, product_data: ProductUpdate) -> Product:
        product = self.get_product(db, product_id)

        for key, value in product_data.model_dump().items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product

    def delete_product(self, db: Session, product_id: int) -> None:
        product = self.get_product(db, product_id)
        db.delete(product)
        db.commit()
