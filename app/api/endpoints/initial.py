from fastapi import APIRouter

router = APIRouter(
    tags=['Initial'],
    prefix='/'
)


@router.get('')
async def init():
    return {"initial_config": "Its working!"}
