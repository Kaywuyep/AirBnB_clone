#!/usr/bin/python3
"""
creating a unique FileStorage instance
for my application.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
