#!/usr/bin/python3
""" reload file data base every time the app loads """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
