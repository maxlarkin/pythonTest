from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get('/')
def root():
    response = '<h1>Hello, world!</h1>'
    return HTMLResponse(content=response)

@app.get('/file', response_class=FileResponse)
def getFile():
    return FileResponse('./.gitignore')


'''pip unistall -r -f requirements.txt'''
'''uvicorn main:app --reload'''