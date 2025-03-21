#!/usr/bin/env python
# server cannot be changed unless killed then re-run (may be intensional)
# import os

# if os.name == 'posix':
#    os.system('clear')
# else:
#    os.system('cls')

import asyncio

from websockets.asyncio.server import serve

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    async with serve(hello, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
    