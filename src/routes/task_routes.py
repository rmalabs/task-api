from services.task_service import TaskService

service = TaskService()

class TaskRoutes:

    @staticmethod
    def get_tasks():
        return service.get_all_tasks()

    def create_task(data):
        return service.create_task(data)