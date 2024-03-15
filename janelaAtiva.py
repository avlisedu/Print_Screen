import pygetwindow as gw
import pyautogui
import keyboard
import time

def capturar_print(janela):
    # Faz a janela ficar em foco
    janela.activate()
    
    # Captura a tela da janela
    screenshot = pyautogui.screenshot(region=(janela.left, janela.top, janela.width, janela.height))
    
    # Salva a captura de tela com um nome sequencial
    capturar_print.counter += 1
    screenshot.save(f"{capturar_print.counter:03d}.jpeg")

# Inicializa o contador
capturar_print.counter = 0

print("Pressione a seta para a direita para capturar um print da janela ativa. Pressione 'q' para sair.")

# Loop para detectar pressionamento de teclas
while True:
    if keyboard.is_pressed('right'):
        janela_ativa = gw.getActiveWindow()
        capturar_print(janela_ativa)
        print("Print capturado.")
        time.sleep(0.2)  # Evita múltiplos prints se a tecla for mantida pressionada
    elif keyboard.is_pressed('q'):
        print("Encerrando o programa.")
        break
