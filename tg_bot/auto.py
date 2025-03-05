import sqlite3
import datetime
from datetime import datetime, timedelta, timezone
from functools import wraps


def with_db_connection(db_path='../db.sqlite3'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                result = func(cursor, *args, **kwargs)
                return result
        return wrapper
    return decorator
