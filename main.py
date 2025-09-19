from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get('/')
def root():
    response = '<h1>Hello, world!</h1>'
    return HTMLResponse(content=response)

@app.get('/file', response_class=FileResponse)
def getFile():
    return FileResponse('.gitignore')

@app.get('/ids/{id}')
def getID(id: int = Path(le = 100, gt=0)):
    return HTMLResponse('<h1>Your id is: ' + str(id) + '</h1>')

@app.get('/users/{name}')
def getUser(name: str = Path(min_length=2, max_length=100), 
            lastname: str = Query(default = 'Undefined', max_length=100, min_length=0)):
    return HTMLResponse('<h1>' + name + ' ' + lastname + '</h1>')

@app.get('/people')
def getPeople(people: list[str] = Query()):
    return people

'''pip unistall -r -f requirements.txt'''
'''uvicorn main:app --reload'''