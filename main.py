from fastapi import FastAPI, Path
from fastapi.responses import FileResponse

users = [
    {'id': 1, 'name': 'maxim', 'lastname': 'larkin'},
    {'id': 2, 'name': 'oleg', 'lastname': 'samoylov'},
    {'id': 3, 'name': 'andrey', 'lastname': 'mihalenko'},
    {'id': 4, 'name': 'sergey', 'lastname': 'petov'},
    {'id': 5, 'name': 'kirill', 'lastname': 'gulev'}
]


def find_user(id: str):
    for user in users:
        if user['id'] == int(id):
            return user
    return None

app = FastAPI()

@app.get('/')
def index():
    return FileResponse('public/index.html')

@app.get('/api/users')
def get_users():
    return users

@app.get('/api/users/{id}')
def get_user(id: str):
    res = find_user(id)
    return res if res != None else 'User not found'