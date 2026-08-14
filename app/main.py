from fastapi import FastAPI
from app.routes.v1.users import user_router
from app.routes.v1.auth import auth_router


app = FastAPI(title='Trip Bus Booking App')

app.include_router(auth_router)
app.include_router(user_router)
