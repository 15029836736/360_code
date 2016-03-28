#!/usr/bin/env python
import socket
import  sys,time
HOST, PORT = "172.25.39.1", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
   	sock.connect((HOST, PORT))
	while True:
		key=raw_input("input the key what you want: ")
		if key=="q":
			print("		please wait")
			time.sleep(1)
			print("		thanks for use")
			break
		else:
   			sock.sendall(key)
    			received = sock.recv(1024)
			print("		searching ,please wait..")
			time.sleep(1)
    			print("the result is : %s" % received)
except:
	print("connect error")
finally:
	sock.close()
