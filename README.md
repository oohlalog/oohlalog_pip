Oohlalog Python Plugin
======================

## Getting Started

First install Oohlalog from pypi
* pip install Oohlalog

Next initialize the custom logger into your api:

### Python 2.7

```python
import logging
from oohlalog import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))
```

### Python 3

```python
import logging
from py3 import logger

logs = logging.getLogger('test')
logs.addHandler(logger.OohLaLogHandler('API_KEY'))
```

### Test it out!

Here are some sample log calls (same as any logging you already have) that will be forwarded to Oohlalog

```python
logs.info('test info')
logs.debug('test debug')
logs.warning('test warning')
logs.error('test error')
logs.critical('test critical')
```

now go check Oohlalog for the logs

## Oohlalog configuration options:

OohLaLogHandler(apiKey, threshold=100, timeout=5, formatter=None)

__Required__

* __apiKey__ = OohLaLog Api Key

__Optional__
* __threshold__ = number of logs before sending to OohLaLog
* __timeout__ = number of seconds to keep logs before sending to OohLaLog (overrides the threshold)
* __formatter__ = logging.Formatter (http://docs.python.org/2/library/logging.html#logging.Formatter) that overrides the default detail string sent to OohLaLog
