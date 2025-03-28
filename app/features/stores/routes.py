from fastapi import APIRouter
from .crud import UserCRUD

router = APIRouter(prefix="/stores", tags=["stores"])
user_crud = UserCRUD()

class Store(BaseModel):
    address: str

@router.get("/")
def root():
    return user_crud.select_all()

# Pass the store as body
@router.post("/add-store") 
def add_product(store: Store):
    return user_crud.add_store(store)