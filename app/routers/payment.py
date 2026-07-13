from fastapi import APIRouter, status, Depends
from app.schemas import PaymentCreate, PaymentUpdate, PaymentResponse
from app.services import PaymentService
from app.dependencies import get_payment_service

router = APIRouter(prefix="/payments", tags=["payments"])

@router.get("/")
def list_payments(service: PaymentService = Depends(get_payment_service)) -> list[PaymentResponse]:
    return service.list_payments()

@router.get("/{id}")
def get_payment(id: int, service: PaymentService = Depends(get_payment_service)) -> PaymentResponse:
    return service.get_payment(id)

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate, service: PaymentService = Depends(get_payment_service)) -> PaymentResponse:
    return service.create_payment(payment)

@router.put("/{id}", response_model=PaymentResponse, status_code=status.HTTP_200_OK)
def update_payment(id: int, payment: PaymentUpdate, service: PaymentService = Depends(get_payment_service)) -> PaymentResponse:
    return service.update_payment(id, payment)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(id: int, service: PaymentService = Depends(get_payment_service)) -> None:
    service.delete_payment(id)
