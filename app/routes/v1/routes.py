from math import ceil

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.routes import CreateRouteSchema, FilterRouteSchema, GetAllRouteSchema, GetRouteSchema
from app.models.routes import Route
from app.config.database import get_db
from app.schemas.locations import GetLocationSchema
from app.models.locations import Location
from app.models.users import User
from app.services.auth import get_current_user

route_router = APIRouter(
    tags= ["Routes"],
    prefix="/v1/routes"
)


@route_router.post("", response_model=GetRouteSchema)
async def add_route(route: CreateRouteSchema, db: Session=Depends(get_db)):
    new_route = Route(
    leaving_time=route.leaving_time,
    destination_time=route.destination_time,
    location_uuid=route.location_uuid,
    destination_uuid=route.destination_uuid,
    price=route.price,
    leaving_date=route.leaving_date,
    bus_uuid=route.bus_uuid
)

    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    
    
    location = db.query(Location).filter(Location.uuid == new_route.location_uuid).first()
    destination = db.query(Location).filter(Location.uuid == new_route.destination_uuid).first()
    
    return GetRouteSchema(
        uuid= new_route.uuid,
        leaving_time=new_route.leaving_time,
        destination_time=new_route.destination_time,
        location=GetLocationSchema(
            uuid=location.uuid,
            name=location.name
             ),
        destination=GetLocationSchema(
            uuid=destination.uuid,
            name=destination.name
             ),
        price=new_route.price,
        leaving_date=new_route.leaving_date,
        created_time=new_route.created_time,
        bus_uuid=new_route.bus_uuid
        
    )
    
    
    
    
        
@route_router.get("", response_model=GetAllRouteSchema)
async def get_routes(
    db: Session = Depends(get_db),
    filters: FilterRouteSchema = Depends(),
    current_user: User = Depends(get_current_user)
):  
    
    user = db.query(User).filter(User.uuid == current_user.uuid).first()
        
    if not user:
            raise HTTPException(
                status_code=401,
                detail="User not authorized"
            )
            
    all_routes = []
    
    query = db.query(Route);
    
    if filters.uuid is not None:
        query = query.filter(Route.uuid == filters.uuid)
        
    
    if filters.location_uuid is not None:
        query = query.filter(Route.location_uuid == filters.location_uuid)
        
    if filters.destination_uuid is not None:
        query = query.filter(Route.destination_uuid == filters.destination_uuid)
        
        
    if filters.leaving_date is not None:
        query = query.filter(Route.leaving_date == filters.leaving_date)
        
    if filters.leaving_time is not None:
        query= query.filter(Route.leaving_time == filters.leaving_time)
        
    if filters.destination_time is not None:
        query= query.filter(Route.destination_time == filters.destination_time)  
            
    if filters.created_time is not None:
        query= query.filter(Route.created_time == filters.created_time)          
        
    if filters.price is not None:
        query= query.filter(Route.price == filters.price)
        
    if filters.bus_uuid is not None:
        query= query.filter(Route.bus_uuid == filters.bus_uuid)
        
        
    total_count = query.count()
    pages = filters.page
    limit = filters.limit
    total_pages = ceil(total_count/limit)
    offset = (pages -1) * limit  
            
    all_query = query.offset(offset).limit(limit).all()
    
    if not all_query:
                raise HTTPException(
                    status_code=404,
                    detail="Routes not found"
                )        
                             
                     
           
    for route in all_query:
            location = db.query(Location).filter(Location.uuid == route.location_uuid).first()
            destination = db.query(Location).filter(Location.uuid == route.destination_uuid).first()
            all_routes.append(
                GetRouteSchema(
                uuid= route.uuid,
                leaving_time=route.leaving_time,
                destination_time=route.destination_time,
                location=GetLocationSchema(
                    uuid=location.uuid,
                    name=location.name
                    ),
                destination=GetLocationSchema(
                    uuid=destination.uuid,
                    name=destination.name
                    ),
                price=route.price,
                leaving_date=route.leaving_date,
                created_time=route.created_time,
                bus_uuid=route.bus_uuid
        
    )
            )
            

    return GetAllRouteSchema(
        routes=all_routes,
        page=pages,
        limit=limit,
        total_count=total_count,
        total_pages=total_pages,
    )
        
