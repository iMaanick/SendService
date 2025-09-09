from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from app.application.use_cases.sign_up import (
    SignUpRequest,
    SignUpResponse,
    SignUpUseCase,
)

auth_router = APIRouter()


@auth_router.post("/signup")
@inject
async def sign_up(
        request_data: SignUpRequest,
        use_case: FromDishka[SignUpUseCase],
) -> SignUpResponse:
    return await use_case(request_data)
