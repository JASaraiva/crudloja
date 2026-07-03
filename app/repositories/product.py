from sqlalchemy.orm import Session
from sqlalchemy import select
from app.repositories import category
from app.schemas import ProductCreate
from app.models import Product
from fastapi import HTTPException, status


def create_product(db: Session, product: ProductCreate) -> Product:    
    product = Product(**product.model_dump())
    category = category.get_category(db, product.category_id)

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product(db: Session, product_id: int) -> Product:
    stmt = select(Product).where(Product.id == product_id)
    product = db.execute(stmt).scalar_one_or_none()
    
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return product


def list_products(db: Session) -> list[Product]:
    stmt = select(Product)
    return db.execute(stmt).scalars().all()


def update_product(db: Session, product_id: int, product_data: ProductCreate) -> Product:
    product = get_product(db, product_id)
   
    for key, value in product_data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> Product:
    product = get_product(db, product_id)
    
    db.delete(product)
    db.commit()
    return product