# Python Networking Protocols Implementation

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive collection of Python implementations for fundamental networking protocols, designed for learning, experimentation, and educational purposes. This repository demonstrates the core concepts of modern network communication through practical, hands-on examples.

## 🌟 Features

This repository provides production-ready examples of four essential networking protocols:

- **MQTT** - Lightweight publish-subscribe messaging for IoT and real-time applications
- **TCP** - Reliable, connection-oriented communication with guaranteed delivery
- **UDP** - Fast, connectionless communication for time-sensitive applications  
- **WebSocket** - Full-duplex communication for real-time web applications

Each protocol includes both client and server implementations with clear, commented code that's perfect for understanding network communication concepts.

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/networking-protocol-implementation.git
   cd networking-protocol-implementation
   ```

2. **Install dependencies:**
   ```bash
   pip install -e .
   ```
   
   Or manually install required packages:
   ```bash
   pip install paho-mqtt websockets asyncio
   ```

### Running the Examples

Each protocol directory contains ready-to-run examples. Start with any protocol that interests you:

```bash
# TCP Communication
python TCP/tcp_server.py    # Terminal 1: Start server
python TCP/tcp_client.py    # Terminal 2: Start client

# MQTT Messaging
python MQTT/mqtt_publisher.py    # Publish a message
python MQTT/mqtt_subscriber.py   # Subscribe to messages

# UDP Communication
python UDP/udp_receiver.py       # Start listening
python UDP/udp_sender.py         # Send a message

# WebSocket Communication
python WebSocket/websocket_server.py    # Terminal 1: Start server
python WebSocket/websocket_client.py    # Terminal 2: Start client
```

## 📚 Protocol Overview

### MQTT (Message Queuing Telemetry Transport)

**Purpose**: Lightweight publish-subscribe messaging protocol perfect for IoT devices and resource-constrained environments.

**Use Cases**:
- IoT sensor data collection
- Real-time messaging applications
- Remote device monitoring
- Low-bandwidth environments

**Key Features**:
- Quality of Service (QoS) levels (0, 1, 2)
- Retained messages
- Last will and testament
- Topic-based subscriptions

**Example Flow**:
```python
# Publisher
client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.publish("topic/learning", "Hello MQTT!")

# Subscriber
client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("topic/learning")
client.loop_forever()
```

### TCP (Transmission Control Protocol)

**Purpose**: Reliable, connection-oriented communication with guaranteed message delivery and error correction.

**Use Cases**:
- File transfers
- Web browsing (HTTP/HTTPS)
- Email transmission
- Database connections
- Any application requiring guaranteed delivery

**Key Features**:
- Connection establishment and termination
- Error detection and correction
- Flow control and congestion control
- Ordered data delivery

**Example Flow**:
```python
# Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(5)
client_socket, addr = server_socket.accept()
data = client_socket.recv(1024)
client_socket.send("Response".encode())
```

### UDP (User Datagram Protocol)

**Purpose**: Fast, connectionless communication ideal for time-sensitive applications where speed is more important than reliability.

**Use Cases**:
- Video streaming
- Online gaming
- DNS queries
- Real-time audio/video calls
- Network discovery protocols

**Key Features**:
- No connection establishment required
- Lower latency than TCP
- No guaranteed delivery
- Broadcast and multicast support

**Example Flow**:
```python
# Sender
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_socket.sendto("Message".encode(), ('localhost', 12345))

# Receiver
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind(('localhost', 12345))
data, addr = receiver_socket.recvfrom(1024)
```

### WebSocket

**Purpose**: Full-duplex communication protocol enabling real-time, bidirectional communication between client and server.

**Use Cases**:
- Real-time chat applications
- Live data dashboards
- Online multiplayer games
- Collaborative editing tools
- Stock trading platforms

**Key Features**:
- Persistent connection
- Low overhead after handshake
- Real-time bidirectional communication
- Cross-platform compatibility

**Example Flow**:
```python
# Server
async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

# Client
async with websockets.connect("ws://localhost:8765") as websocket:
    await websocket.send("Hello WebSocket!")
    response = await websocket.recv()
```

## 📁 Project Structure

```
networking-protocol-implementation/
├── README.md                    # This file
├── pyproject.toml               # Project configuration and dependencies
├── .python-version              # Python version specification
├── .gitignore                   # Git ignore rules
├── MQTT/                        # MQTT Protocol Implementation
│   ├── mqtt_publisher.py        # Publishes messages to topics
│   └── mqtt_subscriber.py       # Subscribes and receives messages
├── TCP/                         # TCP Protocol Implementation
│   ├── tcp_server.py            # TCP server implementation
│   └── tcp_client.py            # TCP client implementation
├── UDP/                         # UDP Protocol Implementation
│   ├── udp_sender.py            # UDP message sender
│   └── udp_receiver.py          # UDP message receiver
└── WebSocket/                   # WebSocket Protocol Implementation
    ├── websocket_server.py      # WebSocket server with echo functionality
    └── websocket_client.py      # WebSocket client implementation
```

## 🛠️ Development Setup

### Environment Setup

1. **Python Version Management:**
   This project uses Python 3.12+. You can check your version with:
   ```bash
   python --version
   ```

2. **Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

3. **Development Dependencies:**
   ```bash
   pip install -e .[dev]  # If development dependencies are configured
   ```

### Testing the Implementations

Each protocol can be tested independently. Here are some testing strategies:

**Network Testing:**
- Use `localhost` for local testing
- Monitor with tools like `netstat` or `ss` to see active connections
- Use `tcpdump` or Wireshark to analyze network traffic

**MQTT Testing:**
- Install a local MQTT broker like [Mosquitto](https://mosquitto.org/)
- Test with MQTT clients like [MQTT Explorer](https://mqtt-explorer.com/)

**WebSocket Testing:**
- Use browser developer tools or extensions like WebSocket King Client
- Test with online WebSocket testing tools

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **Port Already in Use**
   ```bash
   # Find process using port 9999
   netstat -tulpn | grep :9999  # Linux/Mac
   netstat -ano | findstr :9999  # Windows
   
   # Kill the process or change the port in the code
   ```

2. **MQTT Connection Issues**
   - Ensure an MQTT broker is running (e.g., Mosquitto on port 1883)
   - Check firewall settings
   - Verify broker address in code matches your setup

3. **WebSocket Connection Refused**
   - Start the WebSocket server before the client
   - Check that the WebSocket server is bound to the correct address/port
   - Ensure no firewall is blocking WebSocket connections

4. **Permission Errors**
   - Ports below 1024 require admin privileges on Unix systems
   - Use ports >= 1024 for regular applications
   - On Windows, check if antivirus software is blocking the connection

### Debug Mode

Enable additional logging by adding these lines at the start of your scripts:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🎯 Learning Outcomes

By studying and running these examples, you'll gain understanding of:

- **Network fundamentals**: How different protocols handle communication
- **Client-server architecture**: Understanding roles and responsibilities
- **Error handling**: Managing network failures and recovery
- **Protocol selection**: Choosing the right protocol for your use case
- **Performance considerations**: Latency, throughput, and reliability trade-offs
- **Real-world applications**: How these protocols power modern applications

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- **Bug Reports**: Report issues with clear reproduction steps
- **Feature Requests**: Suggest new protocols or improvements
- **Code Improvements**: Optimize existing implementations
- **Documentation**: Enhance this README or add code comments
- **Examples**: Add real-world use case examples

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📖 Further Reading

- [Python Socket Programming Tutorial](https://docs.python.org/3/library/socket.html)
- [MQTT Protocol Specification](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html)
- [WebSocket API Specification](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
- [Computer Networks by Andrew Tanenbaum](https://www.amazon.com/Computer-Networks-Andrew-Tanenbaum/dp/0132126958)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Python Documentation Team for excellent socket programming guides
- Eclipse Paho MQTT client library contributors
- WebSockets library maintainers
- Open source networking community for educational resources

---

**Happy Networking! 🌍**

*This repository is designed for educational purposes. For production systems, consider using established frameworks, adding proper error handling, security measures, and comprehensive testing.*