from sqlalchemy.orm import sessionmaker


class SQLDBContext(object):

    def __init__(self, engine):
        self.session = None
        self.engine = engine

    def __enter__(self):
        session = sessionmaker()
        self.session = session(bind=self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.rollback()
        self.session.close()