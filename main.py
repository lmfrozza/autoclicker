import pyautogui
import time
import keyboard
import PySimpleGUI as sg


global interval
def click():
    pyautogui.click()

def main(val):
    # Intervalo entre cliques, em segundos
    

    # Loop infinito
    while True:
        # Verifica se o botão de parada ('q') foi pressionado
        if keyboard.is_pressed("q"):
            break

        click()
        time.sleep(float(val))

layout =[
    [sg.Text("Selecione o intervalo:")],
    [sg.InputText(key="intervalo", size= 10), sg.Button("iniciar")],
]
janela=sg.Window("3x3", layout)

while True:
    evento, valor= janela.read()
    if evento==sg.WIN_CLOSED:
        break
    if evento == "iniciar":
        interval = valor["intervalo"]
        main(interval)