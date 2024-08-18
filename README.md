Here's a README.md file tailored for your TCP server and client project in Python 3:

```markdown
# Python TCP Keystroke Logger

This project implements a simple TCP server and client in Python 3. The client listens for keyboard events and sends each keystroke to the server, which logs the received data into a file. This setup can be used for basic remote keystroke logging for educational purposes.

## Features
- **Keystroke Logging:** Captures and sends every keystroke from the client to the server.
- **Data Logging:** The server logs all received keystrokes into a `log.txt` file.
- **Real-Time Communication:** Keystrokes are transmitted immediately upon detection.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries:
  - `pynput`: To listen to keyboard events.
  - `socket`: Built-in Python library for network communication.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lowrek/TCP-Server-Client.git
   cd tcp-keystroke-logger
   ```

2. Install the required library:
   ```bash
   pip install pynput
   ```

### Usage

#### Running the Server
1. Start the TCP server to listen for incoming connections:
   ```bash
   python3 tcp_server.py
   ```
2. The server will display a message when a client connects and log the received keystrokes to `log.txt`.

#### Running the Client
1. Start the TCP client to capture and send keystrokes:
   ```bash
   python3 tcp_client.py
   ```
2. The client will begin sending keystrokes to the server as they are pressed.

### Example

- **Server Output:**
  ```
  Listening for connections...
  Connected by ('127.0.0.1', 54321)
  Received: h
  Received: e
  Received: l
  Received: l
  Received: o
  ```

- **Client Input:**
  - Typing "hello" on the client side sends the characters to the server.

- **Log File (`log.txt`):**
  ```
  h
  e
  l
  l
  o
  ```

### Configuration

- **Server Configuration:**
  - IP Address: `127.0.0.1` (localhost)
  - Port: `9999`
  - Modify these in the server code if needed.

- **Client Configuration:**
  - Server IP Address: `127.0.0.1`
  - Server Port: `9999`
  - Modify these in the client code if needed.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any issues or questions, please open an issue on this repository or contact me at [omarmousa96103@gmail.com]

### Disclaimer

This project is intended for educational purposes only. Unauthorized keystroke logging is illegal and unethical. Use this tool responsibly.
```

This README should help anyone understand your project and get it running quickly.
