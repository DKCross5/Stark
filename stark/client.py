#!/usr/bin/env python

import websockets
from websockets.sync.client import connect

def hello():
    uri = "ws://localhost:8765"
    with connect(uri) as websocket:
        name = "ESP1"

        websocket.send(name)
        print(f">>> {name}")

        greeting = websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    hello()

# if __name__ == "__main__":
#     for _ in range(5):  # Loop to run the function 5 times
#         hello()
