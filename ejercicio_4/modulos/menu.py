from corefiles import updatefile
import modulos.empleado as emp
import modulos.pago as pa
import modulos.reportes as rep

def mainmenu(Nominas):
    global NominasG
    NominasG = Nominas
    while True:
        emp.os.system('cls')
        print('Que deseas hacer?')
        print('1. ingresar empleado \n2. pagar a empleado\n3. reportes\n4. Salir  ')
        op = str(input(')_'))
        if op == '1':
            emp.AddEmpleado(NominasG)
            updatefile('data.json', NominasG)
        elif op == '2':
            pa.PagarEmpleado(NominasG)
            updatefile('data.json', NominasG)
        elif op == '3':
            MenuReportes()
        elif op == '4':
            break
        else:
            print('opcion invalida')
            emp.os.system('pause')

def MenuReportes():
    while True:
        emp.os.system('cls')
        print('Que deseas hacer?')
        print('1. ver total pagado \n2. buscar historial colillas de pago\n3. buscar ultima colilla de pago\n4. salir ')
        op = str(input(')_'))
        if op == '1':
            rep.totasPagar(NominasG)
        elif op == '2':
            rep.historialRep(NominasG)
        elif op == '3':
            pass
        elif op == '4':
            break
        else:
            print('opcion invalida')
            emp.os.system('pause')