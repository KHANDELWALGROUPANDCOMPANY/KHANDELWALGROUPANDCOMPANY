from fastapi import APIRouter

router = APIRouter()

@router.get("/vision")
def get_vision():
    return {
        "vision": "To build a Global AI + Dharma-powered Bharat Network for Humanity"
    }
