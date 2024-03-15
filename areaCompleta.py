import pygetwindow as gw
import pyautogui
import keyboard
import time
from PIL import ImageGrab

def capturar_print():
    # Captura a tela inteira
    screenshot = ImageGrab.grab()
    
    # Salva a captura de tela com um nome sequencial e formato PNG
    capturar_print.counter += 1
    screenshot.save(f"{capturar_print.counter:03d}.png")

# Inicializa o contador
capturar_print.counter = 0

print("Pressione a seta para a direita para capturar um print da tela inteira. Pressione 'q' para sair.")

# Loop para detectar pressionamento de teclas
while True:
    if keyboard.is_pressed('right'):
        capturar_print()
        print("Print capturado.")
        time.sleep(0.2)  # Evita múltiplos prints se a tecla for mantida pressionada
    elif keyboard.is_pressed('q'):
        print("Encerrando o programa.")
        break
