from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.features.authorization.routes import router as auth_router
from app.features.inventory.routes import router as inventory_router
from app.features.payment.routes import router as payment_router
from app.features.products.routes import router as products_router
from app.features.stores.routes import router as stores_router
from app.features.users.routes import router as users_router

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
app.include_router(users_router)
