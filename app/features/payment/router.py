from fastapi import APIRouter

router = APIRouter(prefix="/payment", tags=["payment"])

@router.get("/")
def root():
    return {"message": "Payment Module"}
