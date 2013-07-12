import logging
import urllib.request
import json
import time
import threading
import socket

class OohLaLogHandler(logging.Handler):
	def __init__(self,apiKey, threshold=100, timeout=5,formatter=None):
		logging.Handler.__init__(self)

		self.apiKey = apiKey
		self.threshold = threshold
		self.timeout = timeout
		self.checkerThread = None
		if formatter == None:
			self.formatter = logging.Formatter('An error occured in module %(module)s:%(funcName)s at line %(lineno)d with the message "%(message)s"')
		else:
			self.formatter = formatter
		
		self.logs = []
	def emit(self,record):
		#append a new log dictionary to the list
		self.logs.append({'message':record.msg,'level':record.levelname,'timestamp':int(time.time()*1000),'details':self.formatter.format(record),'category':record.levelname,'hostName':socket.gethostname()});
		self.flush()
	def flush(self,force=False):
		if len(self.logs) >= self.threshold or force and len(self.logs) > 0:
			#start a thread to send off our data
			threading.Thread(target=self.sendToOll).start()
			#checker thread is set to none so we can check again
			self.checkerThread = None
		elif force != True and len(self.logs) > 0 and self.checkerThread == None:
			#check again soon and only if we dont have a checker queued
			self.checkerThread = threading.Timer(self.timeout,self.flush,[True]).start()
	def sendToOll(self):
		headers = {}
		headers['Content-Type'] = 'application/json'
		body = json.dumps({'logs':self.logs})
		body = body.encode('utf-8')
		del self.logs[:]
		conn = urllib.request.urlopen('http://api.oohlalog.com/api/logging/save.json?apiKey=' + self.apiKey,body)
		conn.close()
	def kill(self):
		if self.checkerThread != None:
			self.checkerThread.cancel()
