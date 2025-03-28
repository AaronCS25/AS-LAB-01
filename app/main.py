from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.features.authorization.router import router as auth_router
from app.features.inventory.router import router as inventory_router
from app.features.payment.router import router as payment_router
from app.features.products.router import router as products_router
from app.features.stores.router import router as stores_router

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(inventory_router)
app.include_router(payment_router)
app.include_router(products_router)
app.include_router(stores_router)
