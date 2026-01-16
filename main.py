# import uuid
# from fastapi import FastAPI, Body
# # from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse


# class User:
#     def __init__(self, name, lastname):
#         self.id = str(uuid.uuid4())
#         self.name = name
#         self.lastname = lastname


# users = [User('Максим', 'Ларкин'),
#          User('Олег', 'Самойлов'),
#          User('Олег', 'Михайленков'),
#          User('Сергей', 'Петов'),
#          User('Кирилл', 'Гулев'),
#          User('Антон', 'Мерин'),
#          User('Форве', 'Эмперрор')]
# # Идет 67 день быссмысленного коммита
# print(users)


# def find_user(id: str):
#     for user in users:
#         if user.id == int(id):
#             return user
#     return None


# app = FastAPI()


# # app.mount('/', StaticFiles(directory='public', html=True))
# @app.get("/")
# def index():
#     return FileResponse("public/index.html", )


# @app.get("/api/users")
# def get_users():
#     return users


# @app.get('/api/users/{id}')
# def get_user(id: str):
#     res = find_user(id)
#     return res if res is not None else 'User not found'


# @app.put('/api/users')
# def update_user(data=Body()):
#     user = find_user(data['id'])
#     if user is not None:
#         user['name'] = data['name'] 
#         user['lastname'] = data['lastname']   
#         return user
#     return 'User not found'


# @app.post('/api/users')
# def create_user(data=Body()):
#     user = User(data['name'], data['lastname'])
#     users.append(user)
#     return user

from abc import abstractmethod, ABC


class User(ABC):
    @abstractmethod
    def get_info(self):
        pass


class Admin(User):
    def __init__(self):
        self.id = 1

    def get_info(self):
        return 'admin'

    @property
    def name(self):
        return 'admin' + str(self.id)

    @name.setter
    def name(self, id):
        self.id = int(id)

    def __str__(self):
        return 'admin' + str(self.id)

    def _change_id(self, id):
        self.id = id

    def __id_to_zero(self):
        self.id = 0


obj = Admin()
# obj.__id_to_zero() нет такого метода

print(obj)
