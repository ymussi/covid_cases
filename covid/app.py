from covid.api import api
from covid.api.miner.viewer import ns as cases
# from covid.schedule_jobs import run_schedule
from flask import Flask, Blueprint
from flask_restplus import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, doc=False)
blueprint = Blueprint('api', __name__)

api.init_app(blueprint)
api.add_namespace(cases, "/cases")
app.register_blueprint(blueprint)


cors = CORS(app, resources={r"/*": {"origins": "*"}})

# run_schedule()

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '5000'
    debug = True
    app.run(host, int(port), debug)