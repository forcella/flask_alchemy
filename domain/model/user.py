from typing import List

from domain.model.todo import Todo


class User:
    def __init__(self, _id: int, name: str, email: str, password: str):
        self.to_do_list = {}
        self.id = _id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id:{self.id},name:{self.name},email:{self.email})"

    def set_todo_list(self, todo_list: List[Todo]):
        self.to_do_list = {t.id: t for t in todo_list}
