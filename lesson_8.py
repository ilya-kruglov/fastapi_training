from enum import Enum
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, validator

app = FastAPI()


class Person(BaseModel):
    name: str
    surname: str
    age: Optional[int]
    is_staff: bool = False


class LotCategory(str, Enum):
    PRINTER = 'Принтеры'
    MONITOR = 'Мониторы'
    ADDITIONAL_EQUIPMENT = 'Доп. оборудование'
    INPUT_DEVICES = 'Устройства ввода'


class AuctionLot(BaseModel):
    category: LotCategory
    name: str
    model: Optional[str]
    start_price: int = Field(
        default=None,
        description='Start price, multiple of 1000',
    )
    seller: Person

    @validator('start_price')
    def validate_start_price(cls, value):
        if value is None:
            return None
        if value % 1000 != 0:
            raise ValueError('Start price must be a multiple of 1000')
        return value


@app.post('/new-lot')
def register_lot(lot: AuctionLot):
    # Здесь мог бы быть код для сохранения заявки,
    # но мы не станем его писать. И вам не надо.
    return {'result': 'Ваша заявка зарегистрирована!'}


if __name__ == '__main__':
    uvicorn.run('lesson_8:app', reload=True)
