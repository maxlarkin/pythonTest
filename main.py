from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/')
def root():
    return FileResponse('public/index.html')

@app.post('/api/users')
def userInfo(data = Body(min_length=1)):
    return {'message': f'user: {data["name"]} {data["lastname"]}'}

'''pip unistall -r -f requirements.txt'''
'''uvicorn main:app --reload'''