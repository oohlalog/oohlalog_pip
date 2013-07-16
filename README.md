Oohlalog Python Plugin
======================

**IN ACTIVE DEVELOPMENT**


OohLaLogHandler(apiKey, threshold=100, timeout=5, formatter=None)

__Required__

* __apiKey__ = OohLaLog Api Key

__Optional__
* __threshold__ = number of logs before sending to OohLaLog
* __timeout__ = number of seconds to keep logs before sending to OohLaLog (overrides the threshold)
* __formatter__ = logging.Formatter (http://docs.python.org/2/library/logging.html#logging.Formatter) that overrides the default detail string sent to OohLaLog

## Python 2.7

```python
import logging
from oohlalog import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))
```

## Python 3

```python
import logging
from py3 import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))
```
