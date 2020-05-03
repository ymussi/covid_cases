from sqlalchemy import Column, String, Integer, MetaData, Table, DATETIME, FLOAT
from covid.database import Base, Register, engine

metadata = MetaData()

user = Table('cases_covid', metadata,
Column('id', Integer, primary_key=True, autoincrement=True),
Column('date', DATETIME),
Column('state', String(100)),
Column('city', String(100)),
Column('place_type', String(100)),
Column('confirmed', Integer),
Column('deaths', Integer),
Column('is_last', String(100)),
Column('estimated_population_2019', Integer),
Column('city_ibge_code', Integer),
Column('confirmed_per_100k_inhabitants', FLOAT),
Column('death_rate', FLOAT),
)

# metadata.create_all(engine)


class Cases(Base, Register):

    __tablename__ = "cases_covid"

    index = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATETIME)
    state = Column(String(100))
    city = Column(String(100))
    place_type = Column(String(100))
    confirmed = Column(Integer)
    deaths = Column(Integer)
    is_last = Column(String(100))
    estimated_population_2019 = Column(Integer)
    city_ibge_code = Column(Integer)
    confirmed_per_100k_inhabitants = Column(FLOAT)
    death_rate = Column(FLOAT)