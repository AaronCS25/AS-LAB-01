from fastapi import APIRouter
from .crud import UserCRUD

router = APIRouter(prefix="/products", tags=["products"])
user_crud = UserCRUD()

@router.get("/")
def root():    
    return user_crud.select_all()

@router.get("/promo-products")
def root():
    return user_crud.select_promo_products()

@router.get("/product-by-name/{name}")
def root():
    return user_crud.get_product_by_name(name)
