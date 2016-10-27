import socket
import httplib

TCP_IP = '0.0.0.0'
TCP_PORT = 8000
BUFFER_SIZE = 1024
FILE = "echo.php"
paramDefine = "message"
MSG = "hello!!"
HOST = "localhost:8000"
RESOURCE = "/echo.php?message=%s" % (MSG)
REQ = "GET " + RESOURCE + " HTTP/1.0\r\nHost: " + HOST + "\r\n\r\n"

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.connect(("localhost", TCP_PORT))
tcpsocket.send(REQ)
data = tcpsocket.recv(BUFFER_SIZE)

while (data != ''):
	print "Received data: ", data
	data = tcpsocket.recv(BUFFER_SIZE)

tcpsocket.close()
