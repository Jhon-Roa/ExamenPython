import os
from corefiles import searhEmpleado, Try, Si

def PagarEmpleado(Nominas):
    print('estas son los empleados existentes\nA cual le quieres pagar?')
    for key, value in Nominas['empleados'].items():
        print(f'{key}, {value["nombre"]}')
    id = searhEmpleado(Nominas)
    while True:
        diasTrabajados= Try('int', 'ingrese los dias que traajo el empleado :')
        if diasTrabajados > 30:
            print('estas ingresando mas dias que los del mes')
        else:
            break
    horasExtras= Try('int', 'cuantas horas extra trabajo el empleado')
    valorhoras= horasExtras*5500
    valorDia = Nominas['empleados'][id]['salario']/30
    valorDias= diasTrabajados*valorDia
    if Si('el empleado debe en cafeteria? Si(S/s) No(Enter)'):
        descuentoCaf= Try('float', 'cuanto debe el empleado?')
    else:
        descuentoCaf= float(0)
    if Si('el empleado debe un prestamo? Si(S/s) No(N/n)'):
        cuotaPrestamo= Try('float', 'de cuanto es la cuota del empleado?')
    else:
        cuotaPrestamo= float(0)
    mesPagado= str(input('cual fue el mes pagado?'))
    while True:
        dia= Try('int', 'que dia es?')
        if dia <= 30 and dia > 0:
            diaS= str(dia).zfill(2)
            if len(diaS) <= 2 and len(diaS) >0:
                break
            else:
                print('ingrese un dia valido')
                os.system('pause')
        else:
            print('ingrese un dia valido')
            os.system('pause')
    while True:
        mes= Try('int', 'que mes es?')
        if mes <= 12 and mes > 0:
            mesS= str(mes).zfill(2)
            if len(mesS) <= 2 and len(mesS) >0:
                break
            else:
                print('ingrese un mes valido')
                os.system('pause')
        else:
            print('ingrese un mes valido')
            os.system('pause')
    while True:
        año= Try('int', 'que año es?')
        añoS= str(año).zfill(4)
        if len(añoS) <= 4 and len(añoS) >0:
            break
        else:
            print('ingrese un año valido')
            os.system('pause')
    fechaDePago= str(f'{diaS}/{mesS}/{añoS}')
    totalPagar= (valorDias+valorhoras)-(cuotaPrestamo+descuentoCaf)
    colDePago= {
        'mes pagado': mesPagado,
        'fecha de pago': fechaDePago,
        'sueldoBase': Nominas['empleados'][id]['salario'],
        'valorTotalHorasExtra': valorhoras,
        'cuotaPrestamo': cuotaPrestamo,
        'descuentoCaf': descuentoCaf,
        'totalPagar': totalPagar
    }
    Nominas['empleados'][id]['col de pago'].append(colDePago)
    