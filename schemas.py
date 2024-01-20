import re
from enum import Enum, IntEnum
from typing import Optional, Union

from pydantic import BaseModel, Field, root_validator, validator


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
    age: Optional[int] = Field(None, gt=4, le=99)
    is_staff: bool = Field(False, alias='is-staff')
    education_level: Optional[EducationLevel]

    class Config:
        title = 'Class for greetings'
        min_anystr_length = 2

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
