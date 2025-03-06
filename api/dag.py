from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db_session
from api.dag_dto import Dag

dag_router = APIRouter()

@dag_router.post('/', response_model=DagDto)
async def create_dag(body: DagDto, session: AsyncSession = Depends(get_db_session)) -> DagDto:
    pass