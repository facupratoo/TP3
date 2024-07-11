import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 91218))
s.send("Hola, servidor".encode())
response = s.recv(1024).decode()
print(response)