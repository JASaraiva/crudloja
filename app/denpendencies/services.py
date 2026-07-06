from fastapi import Depends
from sqlalchemy.orm import Session
from app.services import ProductService, CategoryService
from app.denpendencies.sessions import get_db


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


def get_category_service(db: Session = Depends(get_db)) -> CategoryService:
    return CategoryService(db)
