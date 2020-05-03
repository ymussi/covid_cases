from sqlalchemy import Column, String, Integer, MetaData, Table, DATETIME, FLOAT
from covid.database import Base, Register, engine

class RawCases(Base, Register):

    __tablename__ = "all_cases"

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

class Cases(Base, Register):
    
    __tablename__ = "cases_covid"

    index = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATETIME)
    state = Column(String(100))
    city = Column(String(100))
    confirmed = Column(Integer)
    deaths = Column(Integer)