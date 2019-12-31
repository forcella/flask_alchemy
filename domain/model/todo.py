class Todo:
    def __init__(self, _id: int, task: str, status: str):
        self.id = _id
        self.task = task
        self.status = status

    def __repr__(self):
        return f"ToDo(id:{self.id},task:{self.task},done:{self.status})"
