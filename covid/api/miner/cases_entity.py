from covid.config.mysql import CadastroDBContext
from covid.database import engine
from covid.database.orm_covid_cases import Cases, RawCases

from sqlalchemy.sql import func, label, distinct

import pandas as pd
import io

class CovidEntityCasesRaw:

    def __init__(self):
        self.raw_cases = "all_cases"

    def save_raw_cases(self, data):
        df = pd.DataFrame(data)
        df['confirmed'].astype(int)
        df['deaths'].astype(int)
        resp = df.to_sql(self.raw_cases, engine, if_exists='replace')

        return resp

class CovidEntityCases:

    def __init__(self):
        self.cases_covid = "cases_covid"

    def save_cases_formated(self, data):
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

    def get_city_cases(self, city):
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

    def get_state_cases(self, state):
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
