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


def get_user_pictures(user_id):
    session = Session(bind=engine)

    queryset = session.query(Picture.title, Picture.id).filter(Picture.user_id == user_id)

    session.close()
    return queryset

def get_picture_by_id(picture_id):
    session = Session(bind=engine)
    picture = session.query(Picture).get(picture_id)
    print(picture)
    session.close()
    return picture