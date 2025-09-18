from fastapi import FastAPI, Path
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

'''pip unistall -r -f requirements.txt'''
'''uvicorn main:app --reload'''