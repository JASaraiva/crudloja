from fastapi import APIRouter, status, Depends
from app.schemas import PaymentMethodCreate, PaymentMethodUpdate, PaymentMethodResponse
from app.services import PaymentMethodService
from app.dependencies import get_payment_method_service

router = APIRouter(prefix="/payment_methods", tags=["payment_methods"])

@router.get("/")
def list(service: PaymentMethodService = Depends(get_payment_method_service)) -> list[PaymentMethodResponse]:
    return service.list()

@router.get("/{id}")
def get(id: int, service: PaymentMethodService = Depends(get_payment_method_service)) -> PaymentMethodResponse:
    return service.get(id)

@router.post("/", response_model=PaymentMethodResponse, status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodCreate, service: PaymentMethodService = Depends(get_payment_method_service)) -> PaymentMethodResponse:
    return service.create(payment_method)

@router.put("/{id}", response_model=PaymentMethodResponse, status_code=status.HTTP_200_OK)
def update(id: int, payment_method: PaymentMethodUpdate, service: PaymentMethodService = Depends(get_payment_method_service)) -> PaymentMethodResponse:
    return service.update(id, payment_method)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, service: PaymentMethodService = Depends(get_payment_method_service)) -> None:
    service.delete(id)
