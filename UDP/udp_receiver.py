import socket

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345
receiver_socket.bind((host,port))
print(f"UDP Receiver listening on {host}:{port}")

while True:
    # wait to receive data
    data, addr = receiver_socket.recvfrom(1024)
    print(f"Received message from {addr}:{data.decode('utf-8')}")



