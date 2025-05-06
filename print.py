import pyautogui
import keyboard
from PIL import ImageGrab
import time
import os

def obter_coordenadas():
    print("Coloque o mouse no canto SUPERIOR ESQUERDO e pressione ENTER")
    keyboard.wait('enter')
    superior_esquerdo = pyautogui.position()
    print(f"Superior esquerdo: {superior_esquerdo}")

    print("Agora coloque no canto INFERIOR DIREITO e pressione ENTER")
    keyboard.wait('enter')
    inferior_direito = pyautogui.position()
    print(f"Inferior direito: {inferior_direito}")

    return (superior_esquerdo.x, superior_esquerdo.y, inferior_direito.x, inferior_direito.y)

def capturar_quando_seta(bbox):
    contador = 1
    print("Pressione → para capturar (pressione ESC para sair).")
    while True:
        if keyboard.is_pressed('esc'):
            print("Finalizado.")
            break
        if keyboard.is_pressed('right'):
            time.sleep(0.2)  # evitar múltiplas capturas com um só clique
            screenshot = ImageGrab.grab(bbox=bbox)
            nome_arquivo = f"captura_{contador}.png"
            screenshot.save(nome_arquivo)
            print(f"Captura {contador} salva.")
            contador += 1

            # Aguarda a tecla ser solta para evitar capturas duplicadas
            while keyboard.is_pressed('right'):
                time.sleep(0.1)

# Programa principal
if __name__ == "__main__":
    bbox = obter_coordenadas()
    capturar_quando_seta(bbox)
