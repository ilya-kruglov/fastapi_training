import uvicorn
from fastapi import FastAPI, Form


app = FastAPI()


@app.post('/login')
def login(
        username: str = Form(...),
        password: str = Form(...),
):
    return {'username': username}


if __name__ == '__main__':
    uvicorn.run('form:app', reload=True)