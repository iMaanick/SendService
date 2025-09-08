from fastapi import APIRouter

from app.application.use_cases.sign_up import SignUpRequest

auth_router = APIRouter()


@auth_router.post("/signup")
async def sign_up(request_data: SignUpRequest ) -> dict[str, str]:
    return {"status": "ok"}
