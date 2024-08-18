import socket

# Define IP address and port to listen on
LISTEN_IP = '127.0.0.1'  # Listen on all available interfaces
LISTEN_PORT = 9999

# Create a socket to listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((LISTEN_IP, LISTEN_PORT))
    server.listen()
    print('Listening for connections...')
    
    while True:
        conn, addr = server.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(4096)
            if data:
                with open("log.txt", "a") as log_file:
                    log_file.write(data.decode())
                    print(f"Received: {data.decode()}")
