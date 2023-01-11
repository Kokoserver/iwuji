import time

from fastapi import FastAPI
import databases
import sqlalchemy

from backend.core.config import settings


def get_db_url():
    if settings.ENVIRONMENT in ("testing", "test"):
        test_db_url = f"sqlite:///testing.sqlite"
        return test_db_url
    elif settings.ENVIRONMENT not in ("testing", "test"):
        base_url = settings.DATABASE_URI
        return base_url


database_url = get_db_url()

database = databases.Database(database_url)
metadata = sqlalchemy.MetaData(database)
engine = sqlalchemy.create_engine(database_url)


async def connect_database(app: FastAPI) -> None:
    metadata.create_all(engine)
    app.state.database = database
    database_ = app.state.database
    while True:
        try:
            if not database_.is_connected:
                await database_.connect()
                # if settings.DEBUG:
                print("database connected")
                break
        except Exception as _:
            time.sleep(5)


async def disconnect_database(app: FastAPI) -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
        if settings.DEBUG:
            print("database disconnected")
