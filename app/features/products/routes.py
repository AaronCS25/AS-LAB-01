from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def root():
    return {"message": "Product Module"}

@routr.get("/promo-products")
def root():
    return{"message": ""}


@router.get("/product-by-name")
def root():
    return {"message": "Product Module"}

