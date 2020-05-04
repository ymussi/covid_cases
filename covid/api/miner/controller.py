from flask_restplus import Resource
from covid.api import api
from covid.api.miner.controller import CovidCasesRaw
import logging

log = logging.getLogger(__name__)

ns = api.namespace('/cases', description='')

@ns.route('/')
class GetCases(Resource):
    @ns.response(code=400, description='Bad Request')
    def get(self):
        """
        Searches covid19 case records in Brazil and saves the raw data in a database.
        """
        c = CovidCasesRaw()
        resp = c.save_raw_cases()
        c.save_cases_formated()

        return resp

@ns.route('/city-cases')
@ns.route('/city-cases/<string:city>')
class ListCases(Resource):
    @ns.response(code=400, description='Bas Request')
    def get(self, city="São Paulo"):
        """
        Returns cases of covid19 in a specific city.
        """
        c = CovidCasesRaw()
        resp = c.list_city_cases(city)

        return resp

@ns.route('/state-cases')
@ns.route('/state-cases/<string:state>')
class StateCases(Resource):
    @ns.response(code=400, description='Bas Request')
    def get(self, state="SP"):
        """
        Returns cases of covid19 in a specific state.
        """
        c = CovidCasesRaw()
        resp = c.list_state_cases(state)

        return resp