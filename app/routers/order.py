from fastapi import APIRouter, Depends, status

from app.dependencies import get_current_user, get_order_service
from app.schemas import OrderCreate, OrderUpdate, OrderResponse
from app.services import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/")
def list(service: OrderService = Depends(get_order_service)) -> list[OrderResponse]:
    return service.list()


@router.get("/{id}")
def get(id: int, service: OrderService = Depends(get_order_service)) -> OrderResponse:
    return service.get(id)


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create(order: OrderCreate, service: OrderService = Depends(get_order_service)) -> OrderResponse:
    return service.create(order)


@router.put("/{id}", response_model=OrderResponse, status_code=status.HTTP_200_OK)
def update(id: int, order: OrderUpdate, service: OrderService = Depends(get_order_service)) -> OrderResponse:
    return service.update(id, order)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: OrderService = Depends(get_order_service)) -> None:
    service.delete(id)
