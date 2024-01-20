import uvicorn
from fastapi import Body, FastAPI

from schemas import CelestialBodies, Person

app = FastAPI()


@app.get('/get-solar-object-name')
def get_solar_object_name(diameter: CelestialBodies) -> str:
    return CelestialBodies(diameter).name


@app.post('/hello')
def greetings(person: Person = Body(
    ...,
    examples={
        # 1st example
        'single_surname': {
            'summary': 'Одна фамилия',
            'description': 'Одиночная фамилия передаётся строкой',
            'value': {
                'name': 'Taras',
                'surname': 'Belov',
                'age': 20,
                'is_staff': False,
                'education_level': 'Среднее образование'
            }
        },
        # 2nd example
        'multiple_surnames': {
            'summary': 'Несколько фамилий',
            'description': 'Несколько фамилий передаются списком',
            'values': {
                'name': 'Eduardo',
                'surname': ['Santos', 'Tavares'],
                'age': 20,
                'is_staff': False,
                'education_level': 'Высшее образование'
            }
        },
        # 3d example
        'invalid': {
            'summary': 'Некорректный запрос',
            'description': 'Возраст передаётся только целым числом',
            'value': {
                'name': 'Eduardo',
                'surname': ['Santos', 'Tavares'],
                'age': 'forever young',
                'is_staff': False,
                'education_level': 'Среднее специальное образование'
            }
        }
    }
)) -> dict[str, str]:
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
