from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db_config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
