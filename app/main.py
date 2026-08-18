from fastapi import FastAPI
from app.routes.v1.users import user_router
from app.routes.v1.auth import auth_router
from app.routes.v1.routes import route_router
from app.routes.v1.buses import bus_router


app = FastAPI(title='Trip App')

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(route_router)
app.include_router(bus_router)
