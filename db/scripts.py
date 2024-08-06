from sqlalchemy.orm import Session, sessionmaker

from .connection import engine
from .create_schema import Picture


def create_picture_db(title, picture_url, user_id):
    session = Session(bind=engine)

    picture = Picture(
        title=title,
        picture_url=picture_url,
        user_id=user_id
    )

    session.add(picture)
    session.commit()
    session.close()

