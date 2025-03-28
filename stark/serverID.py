#!/usr/bin/env python
# server cannot be changed unless killed then re-run (may be intensional)
# import os

# if os.name == 'posix':
#    os.system('clear')
# else:
#    os.system('cls')
import asyncio
import websockets
import uuid

clients = {}

async def echo(websocket, path):
    client_id = str(uuid.uuid4())
    clients[client_id] = websocket
    print(f"Client {client_id} connected")
    try:
        async for message in websocket:
            print(f"Received message from {client_id}: {message}")
            await websocket.send(f"Echo from {client_id}: {message}")
    except websockets.ConnectionClosed:
        print(f"Client {client_id} disconnected")
    finally:
        del clients[client_id]

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())