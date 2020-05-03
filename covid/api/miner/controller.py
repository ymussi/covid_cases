from covid.config.mysql import CadastroDBContext
from covid.config.conf import Config
from covid.database import engine
from covid.database.orm_covid_cases import Cases

import pandas as pd
import requests
import io

class CovidCasesRaw(object):

    def __init__(self):
        self.URL = Config.get('BRAZILIO_BASE_URL', 'url')
        self.table = "cases_covid"
        self.cases = None

    def get_cases(self):
        resp = requests.get(self.URL)
        urlData = resp.content
        rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))

        self.cases = rawData

    def save_cases(self):
        self.get_cases()
        cases = self.cases
        df = pd.DataFrame(cases)
        try:
            df['confirmed'].astype(int)
            df.to_sql(self.table, engine, if_exists='replace')
            return {
                    "status": True,
                    "msg": "All records have been successfully updated and saved.",
                    "info": "Go to '/cases/list-cases'(default São Paulo) or '/cases/list-cases/<city>' to get the cases of a specific city"
                }
        except Exception as e:
            return {
                "status": False,
                "msg": "error in saving the records.",
                "err": str(e)
            }
    
    def list_cases(self, city):
        try:
            with CadastroDBContext(engine) as db:
                case = db.session.query(Cases).filter(Cases.city == city).first()  
                city_result = {
                    'index': case.index,
                    'date': case.date,
                    'state': case.state,
                    'city': case.city,
                    'confirmed': case.confirmed,
                    'deaths': case.deaths
                }
            return {"status": True, "cases": city_result}
        except Exception as e:
            return {"status": False, "cases": None, "err": str(e)}


if __name__ == "__main__":
    c = CovidCasesRaw()
    c.save_cases()