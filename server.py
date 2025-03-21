import asyncio
import os

import cv2
import mss
import numpy as np
import websockets

ASCII_CHARS = "@%#*+=-:. "
WIDTH = 80  # Largura do terminal


def get_doom_window():
    """Obtém as coordenadas da janela do DOOM."""
    try:
        output = os.popen("wmctrl -lG | grep -i 'DOOM'").read()
        if output:
            parts = output.split()
            return {
                "left": int(parts[2]),
                "top": int(parts[3]),
                "width": int(parts[4]),
                "height": int(parts[5])
            }
    except Exception as e:
        print(f"Erro ao obter janela no Linux: {e}")

    return None


def image_to_ascii(image):
    """Converte um frame da imagem para ASCII."""
    image = cv2.cvtColor(
        image, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza
    height, width = image.shape
    new_height = int(height * (WIDTH / width) * 0.5)
    image = cv2.resize(image, (WIDTH, new_height))

    # Converte pixels para caracteres ASCII corretamente
    ascii_str = ''.join(
        ASCII_CHARS[min(int(pixel) * len(ASCII_CHARS) //
                        256, len(ASCII_CHARS) - 1)]
        for pixel in image.flatten()
    )
    ascii_str = '\n'.join([ascii_str[i:i+WIDTH]
                          for i in range(0, len(ascii_str), WIDTH)])
    return ascii_str


async def capture_and_send(websocket):
    """Captura a janela do DOOM e envia via WebSocket."""
    with mss.mss() as sct:
        while True:
            window = get_doom_window()
            if not window:
                print("Janela do DOOM não encontrada!")
                await asyncio.sleep(1)
                continue

            screenshot = np.array(sct.grab(window))[
                :, :, :3]  # Remove canal alpha
            ascii_frame = image_to_ascii(screenshot)
            await websocket.send(ascii_frame)
            await asyncio.sleep(0.1)


async def server():

    server = await websockets.serve(capture_and_send, "localhost", 8765)
    print("Servidor WebSocket rodando em ws://localhost:8765")
    await server.wait_closed()


async def test():
    with mss.mss() as sct:
        while True:
            window = get_doom_window()
            if not window:
                print("Janela do DOOM não encontrada!")
                await asyncio.sleep(1)
                continue

            screenshot = np.array(sct.grab(window))[
                :, :, :3]  # Remove canal alpha
            ascii_frame = image_to_ascii(screenshot)
            print(ascii_frame)
            await asyncio.sleep(0.1)


if __name__ == "__main__":

    if get_doom_window() is None:
        print("Janela do DOOM não encontrada!")
        exit(1)

    # asyncio.run(test())
    asyncio.run(server())
