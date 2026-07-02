from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas import ProductCreate
from app.models import Product


    

def create_product(db: Session, product: ProductCreate) -> Product:    
    product = Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product(db: Session, product_id: int) -> Product:
    stmt = select(Product).where(Product.id == product_id)
    return db.execute(stmt).scalar_one_or_none()


def list_products(db: Session) -> list[Product]:
    stmt = select(Product)
    return db.execute(stmt).scalars().all()


def update_product(db: Session, product_id: int, product_data: ProductCreate) -> Product | None:
    product = get_product(db, product_id)
    if not product:
        return None
    for key, value in product_data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> Product | None:
    product = get_product(db, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product