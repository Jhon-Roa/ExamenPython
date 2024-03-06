import os
from corefiles import searhEmpleado
from tabulate import tabulate

def totasPagar(nomina):
    os.system('cls')
    totalPagar= 0
    for value in nomina['empleados'].values():
            totalPagar += value['col de pago'][-1]['totalPagar']
    print(f'el total a pagar es {totalPagar}')
    os.system('pause')

def historialRep(Nominas):
    print('estas son los empleados existentes\nA cual le quieres ver las colillas?')
    for key, value in Nominas['empleados'].items():
        print(f'{key}, {value["nombre"]}')
    id = searhEmpleado(Nominas)
    tabla = Nominas['empleados'][id]['col de pago']
    print(tabulate(tabla, headers= 'keys', tablefmt='grid'))
    os.system('pause')