from fastapi import APIRouter

admin_router = APIRouter(
    tags= ["buses"],
    prefix="/v1/buses"
)



@admin_router.post("")
async def add_buses():
    
