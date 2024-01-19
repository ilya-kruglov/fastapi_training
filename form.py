import uvicorn
from fastapi import FastAPI, File, Form, UploadFile


app = FastAPI()


@app.post('/login')
def login(
        username: str = Form(...),
        password: str = Form(...),
        some_file: UploadFile = File(...)
):
    file_content = some_file.file.read().splitlines()
    return {
        'username': username,
        'file_content': file_content,
    }


if __name__ == '__main__':
    uvicorn.run('form:app', reload=True)
