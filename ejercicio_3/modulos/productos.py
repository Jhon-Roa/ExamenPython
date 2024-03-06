import os 
from tabulate import tabulate

def addProducto(productos):
    os.system('cls')
    while True:
        id= str(input('ingrese la id del producto :'))
        if id in productos:
            print('el producto ya existe')
            os.system('pause')
            return
        else:
            break
    nombre= str(input('ingrese los nombre del producto :'))
    while True:
        try:
            valor= float(input('ingrese el valor del producto :'))
        except ValueError:
            print('valor ingresado invalido ')
            os.system('pause')
        else:
            break
    while True:
        try:
            stockMin= int(input('ingrese la stockMin del producto :'))
            stockMax= int(input('ingrese la stockMax del producto :'))
        except ValueError:
            print('el stock min o max ingresadas no son un numero entero')
            os.system('pause')
        else:
            break
    producto = {
        'id': id,
        'nombre': nombre,
        'valor': valor,
        'stockMin': stockMin,
        'stockMax': stockMax
    }
    productos.update({id: producto})

def tablaProducto(productos):
    tabla = []
    for values in productos.values():
        tabla.append(values)
    print(tabulate(tabla, headers= 'keys', tablefmt='grid'))
    os.system('pause')