from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.routes import CreateRouteSchema, GetRouteSchema
from app.models.routes import Route
from app.config.database import get_db

route_router = APIRouter(
    tags= ["routes"],
    prefix="/v1/routes"
)


@route_router.post("", response_model=GetRouteSchema)
async def add_route(route: CreateRouteSchema, db: Session=Depends(get_db)):
    new_route = Route(
    leaving_time=route.leaving_time,
    destination_time=route.destination_time,
    location=route.location,
    destination=route.destination,
    price=route.price,
    leaving_date=route.leaving_date,
    bus_uuid=route.bus_uuid
)

    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    
    return new_route
    
    
    
    
        
@route_router.get("", response_model=list[GetRouteSchema])
async def get_routes(
    db: Session = Depends(get_db)
):
    all_routes = db.query(Route).all()

    return all_routes
        
