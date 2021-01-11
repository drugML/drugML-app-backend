import os
import logging

from flask import Flask, jsonify, Blueprint
from flask_restplus import Api

from resources.drug import drug_ns

application = Flask(__name__)
api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint, title='Drug Classifier API', doc='/swagger')

api.add_namespace(drug_ns)

application.register_blueprint(api_blueprint)

"""
Custom logger configuration
"""
log_handler = logging.FileHandler('app.log')
log_handler.setLevel(logging.WARNING)
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_format)
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)


# determine local or production db
if application.env == "production":
    # if in production env
    logger.warning('Cloud Database Connected')
else:
    # if in dev env
    logger.warning('Local Database Connected')


@application.route('/')
def index():
    return 'Hellow World!'


# run the app.
if __name__ == "__main__":
    application.run()
