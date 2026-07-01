from sqlalchemy.orm import Session
from app.schemas import ProductCreate
from app.models import Product

def create_product(db: Session, product: ProductCreate) -> Product:    
    product = Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product