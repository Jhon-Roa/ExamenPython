import os

def Try(valor, tipo):
    if tipo == 'float':
        try:
            float(valor)
        except:
            print('valor ingresado es invalido')
            os.system('pause')
            return True
        else:
            return False
    elif tipo == 'int':
        try:
            int(valor)
        except:
            print('valor ingresado es invalido')
            os.system('pause')
            return True
        else:
            return False

def CopUsd():
    isValueTrue = True
    while isValueTrue:
        pesos = input('cuantos pesos quieres convertir a dolar :')
        isValueTrue = Try(pesos, 'float')
    pesosF = float(pesos)
    dolar = pesosF / 3944
    print(f'{pesos}$ pesos colombianos, convertidos a dolar es {dolar}$')
    os.system('pause')

def CopEur():
    isValueTrue = True
    while isValueTrue:
        pesos = input('cuantos pesos quieres convertir a Euros :')
        isValueTrue = Try(pesos, 'float')
    pesosF = float(pesos)
    Euro = pesosF / 4279
    print(f'{pesos}$ pesos colombianos, convertidos a Euros es {Euro}$')
    os.system('pause')

def EurCop():
    isValueTrue = True
    while isValueTrue:
        euros = input('cuantos euros quieres convertir a Pesos :')
        isValueTrue = Try(euros, 'float')
    EurF = float(euros)
    pesos = EurF * 4279
    print(f'{euros}$ euros, convertidos a Pesos colombianos es {pesos}$')
    os.system('pause')

def CopYen():
    isValueTrue = True
    while isValueTrue:
        pesos = input('cuantos pesos quieres convertir a Yenes :')
        isValueTrue = Try(pesos, 'float')
    pesosF = float(pesos)
    Yen = pesosF / 26.30
    print(f'{pesos}$ pesos colombianos, convertidos a Yenes es {Yen}$')
    os.system('pause')