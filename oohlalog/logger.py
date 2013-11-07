from __future__ import with_statement # 2.5 only
import logging
import httplib
import json
import time
import threading
import socket


class OohLaLogHandler(logging.Handler):
	def __init__(self,apiKey, threshold=100, timeout=5,formatter=None, maxThreads=5):
		logging.Handler.__init__(self)

		self.apiKey = apiKey
		self.threshold = threshold
		self.initialThreshold = threshold
		self.runningThreads = 0
		self.maxThreads = maxThreads
		self.threadLock = threading.Lock()
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
		with self.threadLock:
			if len(self.logs) >= self.threshold or force and len(self.logs) > 0:
				#start a thread to send off our data				
				if self.runningThreads > self.maxThreads:
					self.threshold = self.threshold * 10 #increase threshold by order of magnitude
				else:
                                        #Ok to start a new thread to dump things out so that we don't fork bomb the system under load
					self.runningThreads += 1
					threading.Thread(target=self.sendToOll,args=[self.logs]).start()
					self.logs = [] #Re-assign logs because we have started a sending thread if we rely on self.logs in the sending thread and another thread starts we may send duplicate data 
				#checker thread is set to none so we can check again
				self.checkerThread = None
			elif force != True and len(self.logs) > 0 and self.checkerThread is None:
				#check again soon and only if we dont have a checker queued
				self.checkerThread = threading.Timer(self.timeout,self.flush,[True])
				self.checkerThread.start()

	def sendToOll(self,logsToSend):
		headers = {}
		headers['Content-Type'] = 'application/json'
		body = json.dumps({'logs':logsToSend})
		conn = httplib.HTTPConnection('api.oohlalog.com',80)
		conn.request('POST','/api/logging/save.json?apiKey=' + self.apiKey,body,headers)
		response = conn.getresponse()
		conn.close()
		with self.threadLock:
			self.runningThreads -= 1 #Decrement the thread count so that we can start a new thread if we are waiting
		        #Reset the threshold
			if self.threshold > self.initialThreshold:
				self.threshold = self.initialThreshold
	def kill(self):
		if self.checkerThread != None:
			self.checkerThread.cancel()

