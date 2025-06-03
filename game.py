from colorama import Fore
import keyboard
import os
import time
import grafo
import random

tabuleiro = [
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
]

for index_linha in range(len(tabuleiro)):
    for index_casa in range(len(tabuleiro[index_linha])):
        se_for_3_vira_fogo = random.randint(1,5)
        if se_for_3_vira_fogo == 3:
            tabuleiro[index_linha][index_casa] = '🔥'
        else:
            tabuleiro[index_linha][index_casa] = '🌲'

pos_jogador = (0, 0)
icon_jogador = '🚶'

def exibir_tabuleiro():
    os.system("cls")
    for index_linha in range(len(tabuleiro)):
        for index_casa in range(len(tabuleiro[index_linha])):

            if (index_linha, index_casa) == pos_jogador:
                print(icon_jogador, end=' ')
            else:
                print(tabuleiro[index_linha][index_casa], end=' ')
        print()
    time.sleep(0.07)


def mover_jogador():
    global pos_jogador

    linha, coluna = pos_jogador

    if keyboard.is_pressed("w") and linha > 0:
        linha = linha - 1
        pos_jogador = (linha, coluna)
    elif keyboard.is_pressed("s") and linha < len(tabuleiro) - 1:
        linha = linha + 1
        pos_jogador = (linha, coluna)
    elif keyboard.is_pressed("a") and coluna > 0:
        coluna = coluna - 1
        pos_jogador = (linha, coluna)
    elif keyboard.is_pressed("d") and coluna < len(tabuleiro[0]) - 1:
        coluna = coluna + 1
        pos_jogador = (linha, coluna)


def apagar_fogo():
    global pos_jogador
    global icon_jogador

    linha, coluna = pos_jogador

    if keyboard.is_pressed("space") and tabuleiro[linha][coluna] == "🔥":
        tabuleiro[linha][coluna] = "🌲"
        icon_jogador = '💦'


def reset_icon_jogador():
    global icon_jogador

    if icon_jogador == '💦':
        icon_jogador = '🚶'
        time.sleep(0.2)


def check_game_over() -> bool:
    over = True

    for linha in tabuleiro:
        if '🔥' in linha:
            over = False
    
    return over

def jogar():
    os.system("cls")
    print(Fore.CYAN + "Utilize " + Fore.RED + "'W', 'A', 'S', 'D'" + Fore.CYAN + " para se movimentar")
    print(Fore.CYAN + "Aperte " + Fore.RED + "[SPACE]" + Fore.CYAN + " para apagar o fogo em focos.")
    input(Fore.RESET + "\nPressione [ENTER] para continuar.")

    
    exibir_tabuleiro()
    while True:
        mover_jogador()
        apagar_fogo()
        exibir_tabuleiro()
        reset_icon_jogador()
        if check_game_over() == True:
            break
    exibir_tabuleiro()
    print(Fore.CYAN + "\n🎉 Todos os incêndios foram apagados. Parabéns, você salvou a floresta!")
    print(Fore.GREEN + "🌳 As árvores agradecem sua coragem e rapidez! 💚")
    input(Fore.RESET + "\nPressione [ENTER] para continuar")
        

if __name__ == "__main__":
    while True:
        os.system("cls")
        print(Fore.CYAN + " +--+ SAVE THE FOREST +--+ ")
        print(Fore.GREEN + "   Global Solution 2025.1")
        print(Fore.CYAN + "\n(1) - " + Fore.RESET + "Jogar o mini game")
        print(Fore.CYAN + "(2) - " + Fore.RESET +"Rota mais rápida até o incêndio")
        print(Fore.CYAN + "(3) - " + Fore.RESET +"Sair")
        option = input("\n> ")

        match option:
            case "1":
                jogar()
            case "2":
                os.system("cls")
                grafo.jogar_grafo()
            case "3":
                break
            case _:
                print(Fore.RED + "Opção inválida!")
                time.sleep(0.7)

    print(Fore.CYAN + "\nAté logo! 🌳")
    print(Fore.RESET)
    time.sleep(0.9)
    os.system("cls")