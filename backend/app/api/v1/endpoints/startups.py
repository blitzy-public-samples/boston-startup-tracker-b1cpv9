from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.startup import Startup, StartupCreate, StartupUpdate
from app.services.crud_startup import CRUDStartup
from app.utils.dependencies import get_startup_service

router = APIRouter()

@router.get("/", response_model=List[Startup])
def get_startups(startup_service: CRUDStartup = Depends(get_startup_service)) -> List[Startup]:
    """
    Endpoint to retrieve all startups.
    """
    # Call the `get_all` function from the `startup_service` to retrieve all startups
    startups = startup_service.get_all()
    # Return the list of startups
    return startups

@router.get("/{startup_id}", response_model=Startup)
def get_startup(startup_id: int, startup_service: CRUDStartup = Depends(get_startup_service)) -> Startup:
    """
    Endpoint to retrieve a specific startup by ID.
    """
    # Call the `get` function from the `startup_service` to retrieve the startup with the specified ID
    startup = startup_service.get(startup_id)
    # If the startup is not found, raise an HTTPException with status code 404
    if startup is None:
        raise HTTPException(status_code=404, detail="Startup not found")
    # Return the startup
    return startup

@router.post("/", response_model=Startup, status_code=status.HTTP_201_CREATED)
def create_startup(startup_in: StartupCreate, startup_service: CRUDStartup = Depends(get_startup_service)) -> Startup:
    """
    Endpoint to create a new startup.
    """
    # Call the `create` function from the `startup_service` to create a new startup with the provided data
    new_startup = startup_service.create(startup_in)
    # Return the newly created startup
    return new_startup

@router.put("/{startup_id}", response_model=Startup)
def update_startup(startup_id: int, startup_in: StartupUpdate, startup_service: CRUDStartup = Depends(get_startup_service)) -> Startup:
    """
    Endpoint to update an existing startup.
    """
    # Call the `get` function from the `startup_service` to retrieve the startup with the specified ID
    existing_startup = startup_service.get(startup_id)
    # If the startup is not found, raise an HTTPException with status code 404
    if existing_startup is None:
        raise HTTPException(status_code=404, detail="Startup not found")
    # Call the `update` function from the `startup_service` to update the startup with the provided data
    updated_startup = startup_service.update(startup_id, startup_in)
    # Return the updated startup
    return updated_startup

@router.delete("/{startup_id}", response_model=Startup)
def delete_startup(startup_id: int, startup_service: CRUDStartup = Depends(get_startup_service)) -> Startup:
    """
    Endpoint to delete a startup.
    """
    # Call the `get` function from the `startup_service` to retrieve the startup with the specified ID
    existing_startup = startup_service.get(startup_id)
    # If the startup is not found, raise an HTTPException with status code 404
    if existing_startup is None:
        raise HTTPException(status_code=404, detail="Startup not found")
    # Call the `remove` function from the `startup_service` to delete the startup
    deleted_startup = startup_service.remove(startup_id)
    # Return the deleted startup
    return deleted_startup