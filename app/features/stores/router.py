from fastapi import APIRouter

router = APIRouter(prefix="/stores", tags=["stores"])

@router.get("/")
def root():
    return {"message": "Stores Module"}
