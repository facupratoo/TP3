import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind(('127.0.0.1', 12345))

    print("UDP Server esta escuchando 127.0.0.1:12345")

    while True:
        data, addr = s.recvfrom(1024)
        if data:
            print(f"Received from {addr}: {data.decode()}")

            message = 'mensaje para el cliente'
            s.sendto(message.encode(), addr)

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    s.close()