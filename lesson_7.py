import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get(
    '/math-sum'
)
def math_sum(
        add: list[float] = Query(
            ..., gt=0, le=9.99,
            title='Слагаемые', description='Список дробных чисел (float)'
        )
) -> float:
    numbers = [number for number in add]
    return round(sum(numbers), 2)


if __name__ == '__main__':
    uvicorn.run('lesson_7:app', reload=True)
