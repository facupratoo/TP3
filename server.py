import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',91218))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall('Message for client'.encode())
print(data)