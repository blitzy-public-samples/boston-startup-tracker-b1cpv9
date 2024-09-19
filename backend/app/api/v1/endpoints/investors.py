from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.investor import Investor, InvestorCreate, InvestorUpdate
from app.services.crud_investor import CRUDInvestor
from app.utils.dependencies import get_investor_service

router = APIRouter()

@router.get("/", response_model=List[Investor])
def get_investors(investor_service: CRUDInvestor = Depends(get_investor_service)) -> List[Investor]:
    """
    Endpoint to retrieve all investors.
    """
    # Call the `get_all` function from the `investor_service` to retrieve all investors
    investors = investor_service.get_all()
    # Return the list of investors
    return investors

@router.get("/{investor_id}", response_model=Investor)
def get_investor(investor_id: int, investor_service: CRUDInvestor = Depends(get_investor_service)) -> Investor:
    """
    Endpoint to retrieve a specific investor by ID.
    """
    # Call the `get` function from the `investor_service` to retrieve the investor with the specified ID
    investor = investor_service.get(investor_id)
    # If the investor is not found, raise an HTTPException with status code 404
    if not investor:
        raise HTTPException(status_code=404, detail="Investor not found")
    # Return the investor
    return investor

@router.post("/", response_model=Investor, status_code=status.HTTP_201_CREATED)
def create_investor(investor_in: InvestorCreate, investor_service: CRUDInvestor = Depends(get_investor_service)) -> Investor:
    """
    Endpoint to create a new investor.
    """
    # Call the `create` function from the `investor_service` to create a new investor with the provided data
    new_investor = investor_service.create(investor_in)
    # Return the newly created investor
    return new_investor

@router.put("/{investor_id}", response_model=Investor)
def update_investor(investor_id: int, investor_in: InvestorUpdate, investor_service: CRUDInvestor = Depends(get_investor_service)) -> Investor:
    """
    Endpoint to update an existing investor.
    """
    # Call the `get` function from the `investor_service` to retrieve the investor with the specified ID
    existing_investor = investor_service.get(investor_id)
    # If the investor is not found, raise an HTTPException with status code 404
    if not existing_investor:
        raise HTTPException(status_code=404, detail="Investor not found")
    # Call the `update` function from the `investor_service` to update the investor with the provided data
    updated_investor = investor_service.update(existing_investor, investor_in)
    # Return the updated investor
    return updated_investor

@router.delete("/{investor_id}", response_model=Investor)
def delete_investor(investor_id: int, investor_service: CRUDInvestor = Depends(get_investor_service)) -> Investor:
    """
    Endpoint to delete an investor.
    """
    # Call the `get` function from the `investor_service` to retrieve the investor with the specified ID
    existing_investor = investor_service.get(investor_id)
    # If the investor is not found, raise an HTTPException with status code 404
    if not existing_investor:
        raise HTTPException(status_code=404, detail="Investor not found")
    # Call the `remove` function from the `investor_service` to delete the investor
    deleted_investor = investor_service.remove(existing_investor)
    # Return the deleted investor
    return deleted_investor