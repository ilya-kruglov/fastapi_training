import uvicorn
from fastapi import FastAPI

from app.api.endpoints import router

app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
