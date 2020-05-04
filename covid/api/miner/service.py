from covid.api.miner.cases_entity import CovidEntityCases, CovidEntityCasesRaw
from covid.config.conf import Config

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

class SaveCovidCases:

    def save_raw_cases(self):
        """
        Save the data from our database.
        """
        self.get_cases()
        try:
            
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
            
            return {"status": True, "msg": "All records have been successfully updated and saved."}
        except Exception as e:
            return {
                "status": False,
                "msg": "error in saving the records.",
                "err": str(e)
            }

class CovidCases:

    def list_city_cases(self, city):
        """
        Returns cases of covid19 in a specific city.
        """
        try:
            
            return {"status": True, "cases": city_result}
        except Exception as e:
            return {"status": False, "cases": None, "err": str(e)}

    def list_state_cases(self, state):
        """
        Returns cases of covid19 in a specific state.
        """
        try:
            
            return {"status": True, "cases": state_result}
        except Exception as e:
            return {"status": False, "cases": None, "err": str(e)}
