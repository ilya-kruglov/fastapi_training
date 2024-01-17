from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/me")
def hello_author():
    return {"Hello": "author"}


@app.get("/{name}")
def greetings(
        name: str, surname: str, age: Optional[int] = None
) -> dict[str, str]:
    return {"Hello": name.capitalize()}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
