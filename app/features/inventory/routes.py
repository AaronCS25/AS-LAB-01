from fastapi import APIRouter
from .crud import UserCRUD
from pydantic import BaseModel

user_crud = UserCRUD()
router = APIRouter(prefix="/inventory", tags=["inventory"])

class Product(BaseModel):
    id: int
    name: str
    price: float
    is_promo: bool
    quantity: int

# Pass the product as body
@router.post("/add-product") 
def add_product(product: Product):
    return user_crud.add_product(product)

@router.put("/add-inventory/{id}")
def root(id: int, quantity: int = Query(...)):

    return user_crud.add_inventory(id, quantity)

@router.put("/substract-inventory/{id}")
def root(id: int, quantity: int = Query(...)):

    return user_crud.substract_inventory(id,quantity)
