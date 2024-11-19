from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.client.views import get_all_client
from app.models.room.views import get_all_rooms
from app.models.staff.views import get_all_staff


router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/client')
async def get_client_html(request: Request, client=Depends(get_all_client)):
    return templates.TemplateResponse(name='client.html', context={'request': request, 'client': client})

@router.get('/rooms')
async def get_rooms_html(request: Request, rooms=Depends(get_all_rooms)):
    return templates.TemplateResponse(name='rooms.html', context={'request': request, 'rooms': rooms})

@router.get('/staff')
async def get_staff_html(request: Request, staff=Depends(get_all_staff)):
    return templates.TemplateResponse(name='staff.html', context={'request': request, 'staff': staff})