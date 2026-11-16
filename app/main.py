from fastapi import FastAPI
from app.routes.v1.users import user_router
from app.routes.v1.auth import auth_router
from app.routes.v1.routes import route_router
from app.routes.v1.buses import bus_router
from app.routes.v1.locations import location_router
from app.routes.v1.bookings import bookings_router

app = FastAPI(
    title="TRIP App",
    description="TRIP is a bus booking platform backend built with FastAPI. "
                "It provides APIs for user authentication, OTP verification, "
                "and bus booking management.",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(bus_router)
app.include_router(location_router)
app.include_router(route_router)
app.include_router(bookings_router)