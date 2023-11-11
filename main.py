import pyautogui
import time
import keyboard
import PySimpleGUI as sg

velocidades = ["1 CPS","2 CPS","3 CPS","4 CPS","5 CPS","6 CPS","7 CPS","8 CPS"]
global interval

#def click():
    #pyautogui.click()

def main(val):
    # Intervalo entre cliques, em segundos
    

    # Loop infinito
    while True:
        # Verifica se o botão de parada ('q') foi pressionado
        if keyboard.is_pressed("q"):
            break

        pyautogui.click()
        #click()
        time.sleep(float(val))

layout =[
    [sg.Text("Selecione o intervalo:")],
    [sg.Combo(velocidades ,key="intervalo", size= 10), sg.Button("iniciar")],
]

janela=sg.Window("AutoClicker", layout)
 
while True:
    evento, valor= janela.read()
    if evento==sg.WIN_CLOSED:
        break
    if evento == "iniciar":
        if valor["intervalo"] == "1 CPS":
            interval = 1
            print("1")
        if valor["intervalo"] == "2 CPS":
            interval = 0.5
            print("2")
        if valor["intervalo"] == "3 CPS":
            interval = 0.25
            print("3")
        if valor["intervalo"] == "4 CPS":
            interval = 0.125
            print("4")
        if valor["intervalo"] == "5 CPS":
            interval = 0.0625
            print("5")
        if valor["intervalo"] == "6 CPS":
            interval = 0.03125
            print("6")
        if valor["intervalo"] == "7 CPS":
            interval = 0.015625
            print("7")
        if valor["intervalo"] == "8 CPS":
            interval = 0.0078125
            print("8")
        main(interval)

#1 = 1CPS
#0.5 = 2CPS
#0.25 = 3CPS 
#0.125 = 4CPS
#0.0625 = 5CPS
#0.03125 = 6CPS
#0.015625 = 7CPS
#0.0078125 = 8CPS
#0.00390625 = 9CPS