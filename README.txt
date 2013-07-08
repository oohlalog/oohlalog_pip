Oohlalog Python Plugin
======================

**IN ACTIVE DEVELOPMENT**


OohLaLogHandler(apiKey, threshold=100, timeout=5, formatter=None)

[Required]
apiKey = OohLaLog Api Key

[Optional]
threshold = number of logs before sending to OohLaLog
timeout = number of seconds to keep logs before sending to OohLaLog (overrides the threshold)
formatter = logging.Formatter (http://docs.python.org/2/library/logging.html#logging.Formatter) that overrides the default detail string sent to OohLaLog