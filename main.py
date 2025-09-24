from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class TempRequest(BaseModel):
    name: str
    lastname: str = 'Undefined'

@app.get('/')
def root():
    return FileResponse('public/index.html')

@app.post('/api/users')
def userInfo(user: TempRequest):
    return {'message': f'user: 25 {user.name} {user.lastname}'}

'''pip unistall -r -f requirements.txt'''
'''uvicorn main:app --reload'''