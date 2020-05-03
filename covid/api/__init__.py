import logging
import os

from flask_restplus import Api as _Api

log = logging.getLogger(__name__)

v = os.popen('git log | head -n 1')
commit = v.read().replace("commit ", "")[:7]

api = _Api(version='0.1#{}'.format(commit), default='',
            title='', description='')