from fastapi import APIRouter

router = APIRouter(prefix="/authorization", tags=["authorization"])

@router.get("/")
def root():
    return {"message": "Authorization Module"}
