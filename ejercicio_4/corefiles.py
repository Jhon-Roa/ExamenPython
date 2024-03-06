import os
import json

base = 'ejercicio_4/data/'

def checkfile(archivo, data= dict):
    if os.path.isfile(base + archivo):
        with open(base+archivo, 'r') as ar:
            data = json.load(ar)
            return data
    else:
        with open(base+archivo, 'w') as aw:
            json.dump(data, aw, indent= 4)
            return data

def updatefile(archivo, data):
    with open(base+archivo, 'r+') as awr:
        json.dump(data, awr, indent= 4)
        awr.truncate()

def searhEmpleado(nominas):
    if nominas['empleados']:
        while True:
            id= str(input(')_'))
            if id in nominas['empleados']:
                return id
            else:
                print('la id ingresada no existe')
                os.system('pause')
    else:
        print('no hay empleados\n¿A quien le piensas pagar?')
        os.system('pause')
        return

def Try(tipo, msg):
    while True:
        if tipo == 'float':
            try:
                valor= float(input(msg))
            except:
                print('valor ingresado es invalido')
                os.system('pause')
            else:
                return valor
        elif tipo == 'int':
            try:
                valor= int(input(msg))
            except:
                print('valor ingresado es invalido')
                os.system('pause')
            else:
                return valor

def Si(msg):
    while True:
        os.system('cls')
        si= str(input(msg))
        if si == 's' or si == 'S':
            return True
        elif si == '':
            return False
        else:
            print('no estas ingresando s/S o enter')
            os.system('pause')
