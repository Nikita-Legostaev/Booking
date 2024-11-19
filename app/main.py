from fastapi import FastAPI
from app.models.client.views import router as routes_client
from app.models.room.views import router as room_views
from app.models.staff.views import router as staff_views

from app.pages.router import router as router_pages

app = FastAPI()
app.include_router(routes_client)
app.include_router(room_views)
app.include_router(staff_views)
app.include_router(router_pages)
