import uuid
import re
from typing import Optional
from pydantic import BaseModel
from pydantic import validator
from pydantic import constr

class AbstractModel(BaseModel):
    class Config:
        orm_mode = True

class Dag(DtoAbstractModel):
    dag_id: uuid.UUID
    name: str
    