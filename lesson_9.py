from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]


class Person(BaseModel):
    name: str
    surname: str

    @root_validator
    def check_forbidden_names(cls, values):
        full_name = f"{values['name']} {values['surname']}"
        if full_name.lower() in [name.lower() for name in FORBIDDEN_NAMES]:
            raise ValueError('Forbidden name detected')
        return values


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    result = ' '.join([person.name, person.surname])
    result = result.title()
    return {'Hello': result}
