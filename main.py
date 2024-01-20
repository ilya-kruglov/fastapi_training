import uvicorn
from fastapi import FastAPI

from schemas import CelestialBodies, Person

app = FastAPI()


@app.get('/get-solar-object-name')
def get_solar_object_name(diameter: CelestialBodies) -> str:
    return CelestialBodies(diameter).name


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname

    result = ' '.join([person.name, surnames])
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
