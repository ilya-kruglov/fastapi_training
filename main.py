from enum import Enum, IntEnum
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

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


class Person(BaseModel):
    name: str
    surname: list[str]
    age: Optional[int]
    is_staff: bool = False
    education_level: Optional[EducationLevel]


@app.get('/get-solar-object-name')
def get_solar_object_name(diameter: CelestialBodies) -> str:
    return CelestialBodies(diameter).name


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    print(f'person.surname = {person.surname}')
    print(f'person.surname type = {type(person.surname)}')
    print()
    surnames = ' '.join(person.surname)
    print(f'surnames = {surnames}')
    print(f'surnames type = {type(surnames)}')
    print()
    result = ' '.join([person.name, surnames])
    print(f'result = {result}')
    print(f'result type = {type(result)}')
    print()
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
