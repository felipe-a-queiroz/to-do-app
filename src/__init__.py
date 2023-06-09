import os

INITIALIZED_FILE = '.initialized'

if not os.path.exists(INITIALIZED_FILE):
    from .create_db import db
    with open(INITIALIZED_FILE, 'w'):
        pass