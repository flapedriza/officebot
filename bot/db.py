from sqlmodel import SQLModel, create_engine  # noqa: F401

import config
import models  # noqa: F401

sqlite_url = f'sqlite:///{config.DB_PATH}'

engine = create_engine(sqlite_url, echo=True)


def create_tables() -> None:
    print(f'Creating tables on {config.DB_PATH}...')
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
