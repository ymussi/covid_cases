from covid.config.mysql import CadastroDBContext
from covid.config.conf import Config
from covid.database import engine
from covid.database.orm_covid_cases import Cases, RawCases

from sqlalchemy.sql import func, label, distinct
from datetime import datetime

import pandas as pd
import requests
import io

class GetCovidCasesRaw:

    def __init__(self):
        self.URL = Config.get('BRAZILIO_BASE_URL', 'url')
        self.raw_cases = "all_cases"
        self.cases_covid = "cases_covid"
        self.cases = None

    def get_cases(self):
        """
        Get a csv file containing cases of covid19 from brasilIO.
        """
        resp = requests.get(self.URL)
        urlData = resp.content
        rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))

        self.cases = rawData

    def save_raw_cases(self):
        """
        Save the data from our database.
        """
        self.get_cases()
        try:
            df = pd.DataFrame(self.cases)
            df['confirmed'].astype(int)
            df['deaths'].astype(int)
            df.to_sql(self.raw_cases, engine, if_exists='replace')
            return {
                    "status": True,
                    "msg": "All records have been successfully updated and saved.",
                    "info": {
                        "city_cases": "Go to '/cases/city-cases'(default São Paulo) or '/cases/city-cases/<city>' to get the cases of a specific city",
                        "state_cases": "Go to '/cases/state-cases'(default SP) or '/cases/state-cases/<UF>' to get the cases of a specific UF State",
                    }
                }
        except Exception as e:
            return {
                "status": False,
                "msg": "error in saving the records.",
                "err": str(e)
            }
    
    def save_cases_formated(self):
        try:
            with CadastroDBContext(engine) as db:
                cases = db.session.query(RawCases,
                                        label('date', func.max(distinct(RawCases.date))),
                                        label('state', RawCases.state),
                                        label('city', RawCases.city),
                                        label('confirmed', RawCases.confirmed),
                                        label('deaths', RawCases.deaths)).\
                                            group_by(RawCases.city).all()
                
            df = pd.DataFrame(cases)
            del df['RawCases']
            df.to_sql(self.cases_covid, engine, if_exists="replace", index=True)

            return {"status": True, "msg": "All records have been successfully updated and saved."}
        except Exception as e:
            return {
                "status": False,
                "msg": "error in saving the records.",
                "err": str(e)
            }

    def list_city_cases(self, city):
        """
        Returns cases of covid19 in a specific city.
        """
        try:
            with CadastroDBContext(engine) as db:
                case = db.session.query(Cases).filter(Cases.city == city).first()  
                city_result = {
                    'date': case.date,
                    'state': case.state,
                    'city': case.city,
                    'confirmed': case.confirmed,
                    'deaths': case.deaths
                }
            return {"status": True, "cases": city_result}
        except Exception as e:
            return {"status": False, "cases": None, "err": str(e)}

    def list_state_cases(self, state):
        """
        Returns cases of covid19 in a specific state.
        """
        try:
            with CadastroDBContext(engine) as db:
                cases = db.session.query(Cases,
                                        label('date', Cases.date),
                                        label('state', Cases.state),
                                        label('confirmed', func.sum(Cases.confirmed)),
                                        label('deaths', func.sum(Cases.deaths))).\
                                        filter(Cases.state == state).\
                                        group_by(Cases.state).all()[0]
                state_result = {
                    'date': cases.date,
                    'state': cases.state,
                    'confirmed': int(cases.confirmed),
                    'deaths': int(cases.deaths)
                }
            return {"status": True, "cases": state_result}
        except Exception as e:
            return {"status": False, "cases": None, "err": str(e)}

class FormatDfCases:
    pass

class SaveCovidCases:
    pass

class CovidCases:
    pass
