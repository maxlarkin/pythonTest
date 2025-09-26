from fastapi import FastAPI, Path
from fastapi.responses import FileResponse

users = [
    {'id': 1, 'name': 'Максим', 'lastname': 'Ларкин'},
    {'id': 2, 'name': 'Олег', 'lastname': 'Самойлов'},
    {'id': 3, 'name': 'Андрей', 'lastname': 'Михаленко'},
    {'id': 4, 'name': 'Сергей', 'lastname': 'Петов'},
    {'id': 5, 'name': 'Кирилл', 'lastname': 'Гулев'}
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