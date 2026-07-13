from fastapi import Depends
from sqlalchemy.orm import Session
from app.services import ProductService, CategoryService, UserService, OrderService, AdvertisementService, RoleService, PaymentService, CommentService, PaymentMethodService, RatingService
from app.repositories import ProductRepository, CategoryRepository, RoleRepository, CommentRepository, RatingRepository, PaymentMethodRepository, PaymentRepository, UserRepository, OrderRepository, AdvertisementRepository
from app.dependencies.sessions import get_db


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    repository = ProductRepository(db)
    return ProductService(repository)


def get_category_service(db: Session = Depends(get_db)) -> CategoryService:
    repository = CategoryRepository(db)
    return CategoryService(repository)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)


def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    repository = OrderRepository(db)
    return OrderService(repository)


def get_advertisement_service(db: Session = Depends(get_db)) -> AdvertisementService:
    repository = AdvertisementRepository(db)
    return AdvertisementService(repository)


def get_role_service(db: Session = Depends(get_db)) -> RoleService:
    repository = RoleRepository(db)
    return RoleService(repository)


def get_payment_service(db: Session = Depends(get_db)) -> PaymentService:
    repository = PaymentRepository(db)
    return PaymentService(repository)


def get_payment_method_service(db: Session = Depends(get_db)) -> PaymentMethodService:
    repository = PaymentMethodRepository(db)
    return PaymentMethodService(repository)


def get_rating_service(db: Session = Depends(get_db)) -> RatingService:
    repository = RatingRepository(db)
    return RatingService(repository)


def get_comment_service(db: Session = Depends(get_db)) -> CommentService:
    repository = CommentRepository(db)
    return CommentService(repository)