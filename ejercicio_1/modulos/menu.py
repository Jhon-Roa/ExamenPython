import os
import modulos.funciones as fu

def mainmenu():
    while True:
        os.system('cls')
        print('Que deseas hacer?')
        print('1. convertir pesos a dolares\n2. convertir pesos a euros\n3. convertir pesos a pesos\n4. pesos a yenes\n5. Salir  ')
        op = str(input(')_'))
        if op == '1':
            fu.CopUsd()
        elif op == '2':
            fu.CopEur()
        elif op == '3':
            fu.EurCop()
        elif op == '4':
            fu.CopYen()
        elif op == '5':
            break
        else:
            print('opcion invalida igresada')
            os.system('pause')