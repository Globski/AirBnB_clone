#!/usr/bin/python3
"""Initializes FileStorage and reloads data."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
