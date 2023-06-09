from task import Task

class TaskList:
    def __init__(self):
        db.connect()
        db.create_tables([Task])
    
    def create_task(self, description):
        task = Task(description=description)
        task.save()
        return task
    
    def get_task(self, task_id):
        try:
            task = Task.get(Task.id == task_id)
            return task
        except Task.DoesNotExist:
            return None
    
    def get_all_tasks(self):
        return list(Task.select().order_by(Task.completed, Task.id))
    
    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.completed = True
            task.save()
    
    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.delete_instance()
