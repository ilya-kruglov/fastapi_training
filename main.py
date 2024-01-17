import uvicorn

from fastapi import FastAPI

app = FastAPI()


# @app.get("/me")
# def hello_author():
#     return {"Hello": "author"}


@app.get("/{name}")
def greetings(name):
    return {"Hello": name}


@app.get("/me")
def hello_author():
    return {"Hello": "author"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
