from sqlalchemy.orm import Session
from sqlalchemy import select
from app.repositories.category import CategoryRepository
from app.schemas import ProductCreate, ProductUpdate
from app.models import Product
from fastapi import HTTPException, status


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: ProductCreate) -> Product:
        CategoryRepository(self.db).get_category(product.category_id)

        db_product = Product(**product.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product(self, product_id: int) -> Product:
        stmt = select(Product).where(Product.id == product_id)
        product = self.db.execute(stmt).scalar_one_or_none()

        if product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        return product

    def list_products(self) -> list[Product]:
        stmt = select(Product)
        return self.db.execute(stmt).scalars().all()

    def update_product(self, product_id: int, product_data: ProductUpdate) -> Product:
        product = self.get_product(product_id)

        for key, value in product_data.model_dump().items():
            setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> None:
        product = self.get_product(product_id)
        self.db.delete(product)
        self.db.commit()
