import pyautogui
import time
import keyboard

def click():
    pyautogui.click()

def main():
    # Intervalo entre cliques, em segundos
    interval = 0.5

    # Loop infinito
    while True:
        # Verifica se o botão de parada ('q') foi pressionado
        if keyboard.is_pressed("q"):
            break

        click()
        time.sleep(interval)

if __name__ == "__main__":
    main()
