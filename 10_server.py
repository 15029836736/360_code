#!/usr/bin/env python
import SocketServer
import shelve
def dealstr(line):
    line=line.strip()
    str=""
    for i in line:
        if i!=" ":
            str+=i
    return str
class Mythread(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
	pass

class MyHandle(SocketServer.BaseRequestHandler):
    def handle(self):
	while 1:
		self.data = self.request.recv(1024).strip()
        	self.data = dealstr(self.data)
		db=shelve.open("serverdb","r")
		try:
			message=db[self.data]
			self.request.send(message)
		except:
			try:
				message="key not exist"
				self.request.send(message)
			except:
				#print("connect close")
				break
		db.close()

#__main__
db=shelve.open("serverdb")
db.close()
host="172.25.39.1"
port=9999
server = Mythread((host, port), MyHandle)
server.serve_forever()
