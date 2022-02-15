import re
import easygui
print("****Seleccione una opcion****\n1.Cargar Ventas\n2.Cargar Instrucciones\n3.Analizar\n4.Reportes\n5.Salir")
opcion= input()
if opcion == 1:
    ruta = easygui.fileopenbox()
if opcion == 2:
    ruta = easygui.fileopenbox()
if opcion == 3:
    print("holi")
if opcion == 4:
    print("holi")
if opcion == 5:
    exit()
archivoVentas = open('salida.data','r')
archivoInstrucciones = open('prueba.lfp','r')
aV = archivoVentas.read()
aI = archivoInstrucciones.read()

x = re.search(':', aV)

if x is not None:
    Datos = re.split(':', aV, maxsplit=1)
    Mes = Datos[0]
else:
    print("Dato mes no compatible, intente con otro archivo")
    
y = re.search('=', aV)

if y is not None:
    Datos = re.split(':|=', aV)
    año = int(Datos[1])
else:
    print("Dato año no compatible, intente con otro archivo")

z = re.search('\(', aV)

if z is not None:
    Datos = re.split('\(|\)|\[|\]', aV)
else:
    print("Datos de productos no compatibles, intente con otro archivo")
d=0
for j in Datos:
    if not re.search("\"+",j):
        Datos.pop(d)
    d=d+1

archivoInstrucciones.close()
archivoVentas.close()