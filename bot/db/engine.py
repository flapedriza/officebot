from sqlmodel import SQLModel, create_engine  # noqa: F401

import config
from db import models  # noqa: F401

sqlite_url = f'sqlite:///{config.DB_PATH}'

engine = create_engine(sqlite_url, echo=config.ECHO_DB_ACTIONS)


def create_tables() -> None:
    print(f'Creating tables on {config.DB_PATH}...')
    SQLModel.metadata.create_all(engine)
