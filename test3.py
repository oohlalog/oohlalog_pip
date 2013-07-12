import logging
from oohlalog import logger3

logs = logging.getLogger('test')
logs.addHandler(logger3.OohLaLogHandler('API-KEY'))
logs.info('test info')
logs.debug('test debug')
logs.warning('test warning')
logs.error('test error')
logs.critical('test critical')
