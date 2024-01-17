from enum import Enum

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class Tag(str, Enum):
    IMMUTABLE = 'immutable'
    MUTABLE = 'mutable'


@app.post(
    '/a',
    tags=[Tag.IMMUTABLE],
    response_description='Строка',
    summary='Первый пошёл!'
)
def a() -> str:
    """
    **Описание:**

    Это функция A.

    **Возвращает:**

    str: Строка.
    """
    return 'Вот это ответ!'


@app.get(
    '/b',
    tags=[Tag.MUTABLE],
    response_description='Список строк',
    description='Это GET-метод для функции B. Возвращает список строк.',
    summary='Второй пошёл!'
)
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']


@app.post(
    '/c',
    tags=[Tag.IMMUTABLE],
    response_description='Целое число',
    summary='Третий пошёл!'
)
def c() -> int:
    """
    **Описание:**

    Это функция C.

    **Возвращает:**

    int: Целое число.
    """
    return 42


@app.get(
    '/d',
    tags=[Tag.MUTABLE],
    response_description='Словарь',
    description='Это GET-метод для функции D. Возвращает словарь.',
    summary='Четвёртый пошёл!'
)
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}


if __name__ == '__main__':
    uvicorn.run('lesson_6:app', reload=True)
