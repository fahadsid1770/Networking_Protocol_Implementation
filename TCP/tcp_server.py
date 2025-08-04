import socket

#1. Create a socket object
# AF_INET for IPv4, SOCK_STREAM for TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#2. Bind the socket to an address and port
host = "127.0.0.1" #localhost
port = 9999
server_socket.bind((host,port))


#3. Listen for incoming connections (allow up to 5 client to queue up)
server_socket.listen(5)
print(f"TCP Server listening on {host}:{port}")

while True:
    #4. Accept a new connection
    client_socket, addr = server_socket.accept()
    # client_socket, addr = server_socket.accept()
    # print(f"Got a connection from {addr}")

    #5 Receive data from the client (up to 1024 bytes)
    data = client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    #6. Send a response back to the client
    message = "Successfully connected!"
    client_socket.send(message.encode('utf-8'))

    #7. Closing the connection
    client_socket.close()

