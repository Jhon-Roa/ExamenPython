import modulos.productos as pr
from corefiles import updatefile

def mainmenu(usuarios):
    while True:
        pr.os.system('cls')
        print('Que deseas hacer?')
        print('1. ingresar producto \n2. ver productos\n3. Salir  ')
        op = str(input(')_'))
        if op == '1':
            pr.addProducto(usuarios)
            updatefile('productos.json', usuarios)
        elif op == '2':
            pr.tablaProducto(usuarios)
        elif op == '3':
            break
        else:
            print('opcion invalida')
            pr.os.system('pause')