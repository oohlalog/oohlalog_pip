Oohlalog Python Plugin
========================
OohLaLogHandler(apiKey, threshold=100, timeout=5, formatter=None)

Required
------------
apiKey = OohLaLog Api Key

Optional
------------
threshold = number of logs before sending to OohLaLog
timeout = number of seconds to keep logs before sending to OohLaLog (overrides the threshold)
formatter = logging.Formatter (http://docs.python.org/2/library/logging.html#logging.Formatter) that overrides the default detail string sent to OohLaLog

========================
Python 2.7

import logging
from oohlalog import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))

========================
Python 3

import logging
from py3 import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))
