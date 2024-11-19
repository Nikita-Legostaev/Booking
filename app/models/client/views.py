from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.client.repositpries import ClientRepositories
from app.models.client.shemas import SNewClient


router = APIRouter(
    prefix="/client",
    tags=["client"],
)


@router.get("/all")
async def get_all_client(offset: int = 0, limit: int = 10):
    all_client = await ClientRepositories.get_all()
    return all_client[offset:limit]

@router.post("/add_client")
async def add_client(
    SNewClient: SNewClient,
):
    added_client = await ClientRepositories.add(
        full_name=SNewClient.full_name,
        contact=SNewClient.contact,
        passport_number=SNewClient.passport_number,
        registry_date=SNewClient.registry_date,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{client_id}")
async def remove_client(
    client_id: int,
):
    client = await ClientRepositories.find_one_or_none(id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Не найдена")
    await ClientRepositories.delete(id=client_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{client_id}")
async def update_client(
    client_id: int,
    SNewClient: SNewClient,  
    ):
    client = await ClientRepositories.find_by_id(id=client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Не найден")
    await ClientRepositories.update(id=client_id, **SNewClient.model_dump())
    return {"detail": "Успешно изменёно"}
