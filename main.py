import pyautogui
import time
import keyboard

def click():
    pyautogui.click()

def main():
    # Intervalo entre cliques, em segundos
    interval = 0.5

    # Verifica se a tecla 'l' foi pressionada
    # Loop infinito
    while True:
        # Verifica se o botão de parada ('q') foi pressionado
        if keyboard.is_pressed("q"):

        click()
        time.sleep(interval)

            break