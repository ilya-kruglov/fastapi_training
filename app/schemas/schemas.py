import re
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, root_validator, validator


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str = Field(
        ..., max_length=20,
        title='Full name', description='Case-insensitive input is allowed'
    )
    surname: Union[str, list[str]] = Field(..., max_length=50)
    age: Optional[int] = Field(None, gt=4, le=99, example=21)
    is_staff: bool = Field(False, alias='is-staff')
    education_level: Optional[EducationLevel]

    class Config:
        title = 'Class for greetings'
        min_anystr_length = 2
        schema_extra = {
            'examples': {
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
                'multiple_surnames': {
                    'summary': 'Несколько фамилий',
                    'description': 'Несколько фамилий передаются списком',
                    'value': {
                        'name': 'Pablo',
                        'surname': ['Escobar', 'Gaviria'],
                        'age': 74,
                        'is_staff': False,
                        'education_level': 'Среднее образование'
                    }
                },
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
        }

    @validator('name')
    def name_cant_be_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError('The name cannot be a number')
        return value

    @root_validator(skip_on_failure=True)
    def using_different_languages(cls, values):
        surname = ''.join(values['surname'])
        checked_value = values['name'] + surname
        if (re.search('[а-я]', checked_value, re.IGNORECASE)
                and re.search('[a-z]', checked_value, re.IGNORECASE)):
            raise ValueError(
                'Пожалуйста, не смешивайте русские и латинские буквы'
            )
        return values
