import socket

# 1. Create a UDP socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Define the receiver's address and the message
receiver_address = ('127.0.0.1', 12345)
message = "This message is from sender!"

# 3. Send the message (no connect() needed)
sender_socket.sendto(message.encode('utf-8'), receiver_address)
print(f"Sent message to {receiver_address}")

# 4. Close the socket
sender_socket.close()


