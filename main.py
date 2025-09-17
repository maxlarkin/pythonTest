from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def root():
    response = '<h1>Hello, world!</h1>'
    return HTMLResponse(content=response)


'''pip unistall -r -f requirements.txt'''
'''uvicorn main:app --reload'''