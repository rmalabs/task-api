
class TaskStore:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def next_id(self):
        self.counter += 1
        return self.counter

    def save(self, task):
        self.tasks.append(task)

    def get_all(self):
        return self.tasks

    def find(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                return t
        return None 