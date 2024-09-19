from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.funding_round import FundingRound, FundingRoundCreate, FundingRoundUpdate
from app.services.crud_funding_round import CRUDFundingRound
from app.utils.dependencies import get_funding_round_service

router = APIRouter()

@router.get("/", response_model=List[FundingRound])
def get_funding_rounds(
    funding_round_service: CRUDFundingRound = Depends(get_funding_round_service)
) -> List[FundingRound]:
    """
    Endpoint to retrieve all funding rounds.
    """
    # Call the `get_all` function from the `funding_round_service` to retrieve all funding rounds
    funding_rounds = funding_round_service.get_all()
    
    # Return the list of funding rounds
    return funding_rounds

@router.get("/{funding_round_id}", response_model=FundingRound)
def get_funding_round(
    funding_round_id: int,
    funding_round_service: CRUDFundingRound = Depends(get_funding_round_service)
) -> FundingRound:
    """
    Endpoint to retrieve a specific funding round by ID.
    """
    # Call the `get` function from the `funding_round_service` to retrieve the funding round with the specified ID
    funding_round = funding_round_service.get(funding_round_id)
    
    # If the funding round is not found, raise an HTTPException with status code 404
    if funding_round is None:
        raise HTTPException(status_code=404, detail="Funding round not found")
    
    # Return the funding round
    return funding_round

@router.post("/", response_model=FundingRound, status_code=status.HTTP_201_CREATED)
def create_funding_round(
    funding_round_in: FundingRoundCreate,
    funding_round_service: CRUDFundingRound = Depends(get_funding_round_service)
) -> FundingRound:
    """
    Endpoint to create a new funding round.
    """
    # Call the `create` function from the `funding_round_service` to create a new funding round with the provided data
    new_funding_round = funding_round_service.create(funding_round_in)
    
    # Return the newly created funding round
    return new_funding_round

@router.put("/{funding_round_id}", response_model=FundingRound)
def update_funding_round(
    funding_round_id: int,
    funding_round_in: FundingRoundUpdate,
    funding_round_service: CRUDFundingRound = Depends(get_funding_round_service)
) -> FundingRound:
    """
    Endpoint to update an existing funding round.
    """
    # Call the `get` function from the `funding_round_service` to retrieve the funding round with the specified ID
    existing_funding_round = funding_round_service.get(funding_round_id)
    
    # If the funding round is not found, raise an HTTPException with status code 404
    if existing_funding_round is None:
        raise HTTPException(status_code=404, detail="Funding round not found")
    
    # Call the `update` function from the `funding_round_service` to update the funding round with the provided data
    updated_funding_round = funding_round_service.update(funding_round_id, funding_round_in)
    
    # Return the updated funding round
    return updated_funding_round

@router.delete("/{funding_round_id}", response_model=FundingRound)
def delete_funding_round(
    funding_round_id: int,
    funding_round_service: CRUDFundingRound = Depends(get_funding_round_service)
) -> FundingRound:
    """
    Endpoint to delete a funding round.
    """
    # Call the `get` function from the `funding_round_service` to retrieve the funding round with the specified ID
    existing_funding_round = funding_round_service.get(funding_round_id)
    
    # If the funding round is not found, raise an HTTPException with status code 404
    if existing_funding_round is None:
        raise HTTPException(status_code=404, detail="Funding round not found")
    
    # Call the `remove` function from the `funding_round_service` to delete the funding round
    deleted_funding_round = funding_round_service.remove(funding_round_id)
    
    # Return the deleted funding round
    return deleted_funding_round