#!/usr/bin/python3
"""
Instantiates an object of DBStorage or FileStorage
Based on environment variable
"""

from os import environ
store = environ.get('HBNB_TYPE_STORAGE')

if store == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
