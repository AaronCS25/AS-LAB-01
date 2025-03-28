from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/")
def root():
    return {"message": "Inventory Module"}
