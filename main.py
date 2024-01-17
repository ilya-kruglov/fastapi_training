from enum import Enum, IntEnum
from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class CelestialBodies(IntEnum):
    SUN = 1_392_000
    JUPITER = 139_822
    SATURN = 116_464
    URANUS = 50_724
    NEPTUNE = 49_224
    EARTH = 12_742
    VENUS = 12_104
    MARS = 6_780
    GANYMEDE = 5_262
    TITAN = 5_151
    MERCURY = 4_879


@app.get('/get-solar-object-name')
def get_solar_object_name(diameter: CelestialBodies) -> str:
    return CelestialBodies(diameter).name


@app.get("/multiplication")
def multiplication(
        length: int,
        width: int,
        depth: Optional[int] = None
) -> int:
    if depth is not None:
        return int(length * width * depth)
    return int(length * width)


@app.get(
    "/me",
    tags=["special methods", "greetings"],
    summary="Приветствие автора"
)
def hello_author():
    return {"Hello": "author"}


@app.get(
    "/{name}",
    tags=["common methods", "greetings"],
    summary="Общее приветствие",
    response_description="Полная строка приветствия"
)
def greetings(
        *,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False,
        education_level: Optional[EducationLevel] = None,
        name: str,
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """

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
