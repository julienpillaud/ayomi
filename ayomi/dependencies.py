from typing import Iterator

from sqlmodel import Session

from ayomi.database import engine


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
