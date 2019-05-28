# TCP server example
import socket

server_port = 8090
max_users = 5	    #maximum number of queued connections

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", server_port))
server_socket.listen(max_users)

print ("Waiting for client on port ",server_port)

count = 0
while True:
	client_socket, client_address = server_socket.accept()
	print ("connection from ", client_address)
	while True:
		data = client_socket.recv(128)
		if not data:
			break
		print(count, 'received :',data)
		sent = client_socket.send(data)
		if sent == 0:
			print("socket connection broken")
		print(sent)
	print("Disconnected")
	client_socket.close()
	count = count+1

server_socket.close()