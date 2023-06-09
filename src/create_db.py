from .task import db, Task

db.connect()
db.create_tables([Task])
db.close()