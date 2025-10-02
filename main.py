from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

users = [
    {'id': 1, 'name': 'Максим', 'lastname': 'Ларкин'},
    {'id': 2, 'name': 'Олег', 'lastname': 'Самойлов'},
    {'id': 3, 'name': 'Андрей', 'lastname': 'Михаленко'},
    {'id': 4, 'name': 'Сергей', 'lastname': 'Петов'},
    {'id': 5, 'name': 'Кирилл', 'lastname': 'Гулев'},
    {'id': 6, 'name': 'Антон', 'lastname': 'Мерин'},
    {'id': 7, 'name': 'Форве', 'lastname': 'Эмперрор'}
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

@app.put('/api/users')
def update_user(data = Body()):
    user = find_user(data['id'])
    if user != None:
        user['name'] = data['name'] 
        user['lastname'] = data['lastname']   
        return user
    return 'User not found'