from db.memory_store import TaskStore

class TaskService:

    def __init__(self):
        self.store = TaskStore()

    def get_all_tasks(self):
        return self.store.get_all()

    def create_task(self, data):
        task = {
            "id": self.store.next_id(),
            "title": data.get("title"),
            "completed": False
        }
        self.store.save(task)
        return task

    def toggle_task(self, task_id):
        task = self.store.find(task_id)
        task["completed"] = not task["completed"]
        return task