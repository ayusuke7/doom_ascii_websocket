import asyncio

import websockets


async def receive_frames():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            frame = await websocket.recv()
            print("\033c", end="")  # Limpa a tela do terminal
            print(frame)

asyncio.run(receive_frames())
