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
    return db.execute(stmt).first()