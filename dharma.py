from fastapi import APIRouter

router = APIRouter()

@router.get("/dharma")
def get_dharma():
    return {
        "shlok": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन ।",
        "meaning": "You have the right to work only, but never to its fruits."
    }
