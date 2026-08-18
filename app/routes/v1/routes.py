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
async def add_route(bus: CreateRouteSchema, db: Session=Depends(get_db)):
    new_route = Route(
    leaving_time=bus.leaving_time,
    destination_time=bus.destination_time,
    with_ac=bus.with_ac,
    location=bus.location,
    destination=bus.destination,
    price=bus.price,
    leaving_date=bus.leaving_date
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
        
