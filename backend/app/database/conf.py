from fastapi import FastAPI
import databases
import sqlalchemy

from app.core.config import settings

def get_db_url():
    if settings.ENVIRONMENT in  ("testing", "test"):
        test_db_url =  f"sqlite:///testing.sqlite"
        return test_db_url
    elif not settings.ENVIRONMENT in ("testing", "test"):
        database_url = settings.DATABASE_URI
        return database_url

database_url = get_db_url()

database = databases.Database(database_url)
metadata = sqlalchemy.MetaData(database)
engine = sqlalchemy.create_engine(database_url)

    
async def connect_database(app: FastAPI) -> None:
    metadata.create_all(engine)
    app.state.database = database
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
        if settings.DEBUG:
            print("database connected")


async def disconnect_database(app: FastAPI) -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
        if settings.DEBUG:
            print("database disconnected")