from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import database_settings

engine = create_engine(database_settings["default"],
                       convert_unicode=True,
                       echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import your models here
    import models
    Base.metadata.create_all(bind=engine)
