import asyncio
import websockets

async def talk_to_server():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "This message is from the ClientSide.."
        await websocket.send(message)
        print(f"> {message}")

        response = await websocket.recv()
        print(f"Server > {response}")

# Run the client
if __name__ == "__main__":
    asyncio.run(talk_to_server())