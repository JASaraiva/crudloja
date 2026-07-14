from fastapi import APIRouter, status, Depends

from app.schemas import PaymentCreate, PaymentUpdate, PaymentResponse
from app.services import PaymentService
from app.dependencies import get_payment_service

router = APIRouter(prefix="/payments", tags=["payments"])

@router.get("/")
def list(service: PaymentService = Depends(get_payment_service)) -> list[PaymentResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: PaymentService = Depends(get_payment_service)) -> PaymentResponse:
    return service.get(id)

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create(payment: PaymentCreate, service: PaymentService = Depends(get_payment_service)) -> PaymentResponse:
    return service.create(payment)

@router.put("/{id}", response_model=PaymentResponse, status_code=status.HTTP_200_OK)
def update(id: int, payment: PaymentUpdate, service: PaymentService = Depends(get_payment_service)) -> PaymentResponse:
    return service.update(id, payment)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: PaymentService = Depends(get_payment_service)) -> None:
    service.delete(id)
