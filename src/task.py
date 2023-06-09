from peewee import *

db = SqliteDatabase('tasks.db')

class Task(Model):
    description = CharField()
    completed = BooleanField(default=False)

    class Meta:
        database = db

    def __str__(self):
        return f'{self.description} - {"concluída" if self.completed else "pendente"}'