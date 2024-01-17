from enum import Enum
from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get("/multiplication")
def multiplication(
        length: int,
        width: int,
        depth: Optional[int] = None
) -> int:
    if depth is not None:
        return int(length * width * depth)
    return int(length * width)


@app.get("/me")
def hello_author():
    return {"Hello": "author"}


@app.get("/{name}")
def greetings(
        name: str,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False,
        education_level: Optional[EducationLevel] = None,
) -> dict[str, str]:
    result = " ".join([name, surname])
    result = result.title()
    if age is not None:
        result += ", " + str(age)
    if education_level is not None:
        result += ", " + education_level.lower()
    if is_staff:
        result += ", сотрудник"
    return {"Hello": result}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
