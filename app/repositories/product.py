from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, db_product: Product) -> Product:
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product


    def get(self, product_id: int) -> Product | None:
        stmt = select(Product).where(Product.id == product_id)
        return self.db.execute(stmt).scalar_one_or_none()


    def list(self) -> list[Product]:
        stmt = select(Product)
        return self.db.execute(stmt).scalars().all()


    def update(self, product_id: int, product_data: ProductUpdate) -> Product:
        product = self.get_product(product_id)

        for key, value in product_data.model_dump().items():
            setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product


    def delete(self, product_id: int) -> None:
        product = self.get_product(product_id)
        self.db.delete(product)
        self.db.commit()
