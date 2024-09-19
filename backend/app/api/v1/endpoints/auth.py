from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.token import Token
from app.services.auth_service import AuthService
from app.utils.dependencies import get_auth_service

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(
    auth_service: AuthService = Depends(get_auth_service),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Endpoint for user login and access token generation.
    """
    # Authenticate the user using the provided credentials
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generate an access token and refresh token
    access_token = auth_service.create_access_token(data={"sub": user.username})
    refresh_token = auth_service.create_refresh_token(data={"sub": user.username})

    # Return the tokens
    return Token(access_token=access_token, token_type="bearer", refresh_token=refresh_token)