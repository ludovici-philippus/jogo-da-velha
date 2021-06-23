import PySimpleGUI as sg
from random import randint

from PySimpleGUI.PySimpleGUI import Button

vez_player = True
fim = False
jogadas = 0

def player_jogada(event, window):
    global vez_player
    for field in range(1, 10):
        if event == f"F{field}" and window[event].ButtonText != "O" and window[event].ButtonText != "X":
            window[event].update("X")
            vez_player = False
            
def bot_jogada(window):
    global vez_player
    choice = randint(1, 9)
    if window[f"F{choice}"].ButtonText != "X" and window[f"F{choice}"].ButtonText != "O":
        window[f"F{choice}"].update("O")
        vez_player = True
    else:
        bot_jogada(window)

def win(window):
    global fim
    if  (window["F1"].ButtonText == "X" and window["F2"].ButtonText == "X" and window["F3"].ButtonText == "X") or \
        (window["F1"].ButtonText == "X" and window["F4"].ButtonText == "X" and window["F7"].ButtonText == "X") or \
        (window["F1"].ButtonText == "X" and window["F5"].ButtonText == "X" and window["F9"].ButtonText == "X") or \
        (window["F2"].ButtonText == "X" and window["F5"].ButtonText == "X" and window["F8"].ButtonText == "X") or \
        (window["F3"].ButtonText == "X" and window["F6"].ButtonText == "X" and window["F9"].ButtonText == "X") or \
        (window["F3"].ButtonText == "X" and window["F5"].ButtonText == "X" and window["F7"].ButtonText == "X") or \
        (window["F4"].ButtonText == "X" and window["F5"].ButtonText == "X" and window["F6"].ButtonText == "X") or \
        (window["F7"].ButtonText == "X" and window["F8"].ButtonText == "X" and window["F9"].ButtonText == "X"):
        
        sg.popup("You Win!", "Parabéns! Você venceu!")
        fim = True
    
    elif  (window["F1"].ButtonText == "O" and window["F2"].ButtonText == "O" and window["F3"].ButtonText == "O") or \
          (window["F1"].ButtonText == "O" and window["F4"].ButtonText == "O" and window["F7"].ButtonText == "O") or \
          (window["F1"].ButtonText == "O" and window["F5"].ButtonText == "O" and window["F9"].ButtonText == "O") or \
          (window["F2"].ButtonText == "O" and window["F5"].ButtonText == "O" and window["F8"].ButtonText == "O") or \
          (window["F3"].ButtonText == "O" and window["F6"].ButtonText == "O" and window["F9"].ButtonText == "O") or \
          (window["F3"].ButtonText == "O" and window["F5"].ButtonText == "O" and window["F7"].ButtonText == "O") or \
          (window["F4"].ButtonText == "O" and window["F5"].ButtonText == "O" and window["F6"].ButtonText == "O") or \
          (window["F7"].ButtonText == "O" and window["F8"].ButtonText == "O" and window["F9"].ButtonText == "O"):

          sg.popup("You Lose!", "Que pena, parece que você perdeu!")
          fim = True




sg.theme("DarkBlack")
layout = [[sg.Button(key="F1"), sg.Button(key="F2"), sg.Button(key="F3")],
          [sg.Button(key="F4"), sg.Button(key="F5"), sg.Button(key="F6")],
          [sg.Button(key="F7"), sg.Button(key="F8"), sg.Button(key="F9")]]

window = sg.Window("Jogo da Velha", layout)


while not fim:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    if vez_player:
        player_jogada(event, window)
        win(window)
        jogadas += 1
    if not vez_player and jogadas <= 5 and not fim:
        bot_jogada(window)
        win(window)

window.close()
