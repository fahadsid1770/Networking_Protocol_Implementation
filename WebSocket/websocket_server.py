import asyncio
import websockets

# This function handles each client connection
async def echo(websocket):
    print(f"Client connected")
    try:
        # Wait for messages from the client and echo them back
        async for message in websocket:
            print(f"Received message: {message}")
            response = f"Echo: {message}"
            await websocket.send(response)
            print(f"Sent response: {response}")
    except websockets.ConnectionClosed:
        print("Client disconnected.")

async def main():
    # Start the WebSocket server
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server manually stopped.")