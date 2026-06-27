from fastapi import APIRouter, status
from app.schemas import ProductCreate, ProductResponse


router = APIRouter(prefix="/products",
                   tags=["produtos"])

@router.get("/")
def list_products() -> list[dict]:
    return  [
    {
        "id": 1,
        "name": "Notebook"
    },
    {
        "id": 2,
        "name": "Mouse"
    }
]


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product() -> object:
    product_create = ProductCreate()

    return product_create