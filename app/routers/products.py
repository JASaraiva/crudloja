from fastapi import APIRouter
from schemas import ProductCreate

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


@router.post("/")
def create_product() -> object:
    product_create = ProductCreate()

    return product_create