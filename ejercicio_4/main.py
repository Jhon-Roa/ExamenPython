from corefiles import checkfile
from modulos.menu import mainmenu

#notas del algoritmo:
#se puede pagar a los empleados las veces que quiers
#estas se registran en un historial
#pero el total a pagar solo se tomara de la ultima colilla de cada empleado

Nominas= {
    'empleados':{}
}
productos= checkfile('data.json', Nominas)

if __name__ == '__main__':
    mainmenu(Nominas)
    pass