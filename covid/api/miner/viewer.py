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
        resp = c.save_cases()

        return resp

@ns.route('/list-cases')
@ns.route('/list-cases/<string:city>')
class ListCases(Resource):
    @ns.response(code=400, description='Bas Request')
    def get(self, city="São Paulo"):
        """
        List cases by city.
        """
        c = CovidCasesRaw()
        resp = c.list_cases(city)

        return resp