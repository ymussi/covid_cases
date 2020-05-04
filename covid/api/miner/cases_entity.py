from covid.config.mysql import CadastroDBContext
from covid.config.conf import Config
from covid.database import engine
from covid.database.orm_covid_cases import Cases, RawCases

from sqlalchemy.sql import func, label, distinct
from datetime import datetime

import pandas as pd
import requests
import io

class CovidEntityCases:
    pass