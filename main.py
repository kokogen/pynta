import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

import settings
import api.dag

app = FastAPI(title='pynta')


root_api_router = APIRouter()

root_api_router.include_router(dag_router, prefix='/dag', tags=['dag'])

app.include_router(root_api_router)

if __name__ == '__main__':
    uvicorn.run(api, host='localhost', port=APP_PORT)



