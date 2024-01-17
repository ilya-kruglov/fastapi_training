import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
def greetings(name):
    return {"Hello": name}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
