from fastapi import APIRouter

router = APIRouter(prefix = "/categories",
                   tags=["categorias"])

@router.get("/")
def list_categories() -> list[dict]:
    return []