import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind(('127.0.0.1', 91218))

    print("UDP Server esta escuchando 127.0.0.1:")

    while True:
        data, addr = s.recvfrom(1024)
        if data:
            print(f"recibido de {addr}: {data.decode()}")

            message = 'mensaje para el cliente'
            s.sendto(message.encode(), addr)

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    s.close()