from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/add/{id}")
def root():

    return {"message": "Inventory Module"}

@router.get("/update/{id}")
def root():
    
    return {"message": "Inventory Module"}
