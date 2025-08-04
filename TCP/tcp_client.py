import socket

# 1. Creating a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connecting with the server address and port
host = '127.0.0.1'
port = 9999
client_socket.connect((host, port))

# 3. Send a message to the server
message = "Ready to connect!"
client_socket.send(message.encode('utf-8'))

# 4. Receive the response from the server
response = client_socket.recv(1024)
print(f"Server response: {response.decode('utf-8')}")

client_socket.close()