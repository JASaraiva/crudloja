from sqlalchemy.orm import Session
from sqlalchemy import select
from app import repository, models, schemas
from fastapi import HTTPException, status


def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:    
    product = models.Product(**product.model_dump())
    category = repository.get_category(db, product.category_id)

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product(db: Session, product_id: int) -> models.Product:
    stmt = select(models.Product).where(models.Product.id == product_id)
    product = db.execute(stmt).scalar_one_or_none()
    
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return product


def list_products(db: Session) -> list[models.Product]:
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