import os
from sqlalchemy import create_engine
from covid.config.conf import Config
from covid.config.sql import SQLDBContext


def mysql_engine(schema, pool_size=1, max_overflow=25):
    dbname = Config.get("schema", schema)
    con_str = Config.get("database", dbname)
    engine = create_engine("mysql+pymysql://{}/{}".format(con_str, schema),
                           pool_size=pool_size, max_overflow=max_overflow, pool_recycle=30 * 60)
    return engine

class CadastroDBContext(SQLDBContext):

    def __init__(self, engine):
        super().__init__(engine)