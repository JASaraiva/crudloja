from fastapi import APIRouter, status, Depends
from app.schemas import PaymentMethodCreate, PaymentMethodUpdate, PaymentMethodResponse
from app.services import PaymentMethodService
from app.dependencies import get_payment_method_service

router = APIRouter(prefix="/payment_methods", tags=["payment_methods"])

@router.get("/")
def list_payment_methods(service: PaymentMethodService = Depends(get_payment_method_service)) -> list[PaymentMethodResponse]:
    return service.list_payment_methods()

@router.get("/{id}")
def get_payment_method(id: int, service: PaymentMethodService = Depends(get_payment_method_service)) -> PaymentMethodResponse:
    return service.get_payment_method(id)

@router.post("/", response_model=PaymentMethodResponse, status_code=status.HTTP_201_CREATED)
def create_payment_method(payment_method: PaymentMethodCreate, service: PaymentMethodService = Depends(get_payment_method_service)) -> PaymentMethodResponse:
    return service.create_payment_method(payment_method)

@router.put("/{id}", response_model=PaymentMethodResponse, status_code=status.HTTP_200_OK)
def update_payment_method(id: int, payment_method: PaymentMethodUpdate, service: PaymentMethodService = Depends(get_payment_method_service)) -> PaymentMethodResponse:
    return service.update_payment_method(id, payment_method)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment_method(id: int, service: PaymentMethodService = Depends(get_payment_method_service)) -> None:
    service.delete_payment_method(id)
