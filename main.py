from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/me")
def hello_author():
    return {"Hello": "author"}


@app.get("/{name}")
def greetings(
        name: str,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False
) -> dict[str, str]:
    result = " ".join([name, surname])
    result = result.title()
    if age is not None:
        result += ", " + str(age)
    if is_staff:
        result += ", сотрудник"
    return {"Hello": result}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
