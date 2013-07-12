import logging
from py3 import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))
logs.info('test info')
logs.debug('test debug')
logs.warning('test warning')
logs.error('test error')
logs.critical('test critical')
