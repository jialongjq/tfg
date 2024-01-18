import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5555))
server_socket.listen(1)

print("Python script: Waiting for connections...")

while True:
    # Accept a connection from Unity
    conn, addr = server_socket.accept()
    print(f"Connected to Unity at {addr}")

    while True:
        # Receive data from Unity
        data = conn.recv(1024)
        if not data:
            break

        # Process the received data (perform actions based on commands from Unity)
        # Example: execute functions or perform tasks based on the received commands

    conn.close()
