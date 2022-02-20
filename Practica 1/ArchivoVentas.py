import re
from tkinter import Button, Tk, filedialog
from unicodedata import unidata_version
import matplotlib.pyplot as plotpy
import webbrowser

grafica = []
titulo = []
nombre =[]
titulox = []
tituloy = []
productos = []
total = []
Mes = []
año = []
barras = False
lineas = False
pie = False
rutaventas = None
rutainstrucciones = None
pmv = []
pMv = []
precio = []
unidades = []

def menu():
    global rutaventas, rutainstrucciones
    print("****Seleccione una opcion****\n1.Cargar Ventas\n2.Cargar Instrucciones\n3.Analizar\n4.Reportes\n5.Salir")
    op = input()
    
    if op == '1':
        raiz = Tk()
        rutaventas = filedialog.askopenfilename(title="Abrir")
        Button(raiz, text= "abrir archivo" ).pack
        if rutaventas != None:
            cargar_ventas()
            print("ventas cargadas")
            print(Mes)
            print(año)
            print(total)
            print(productos)
            print(len(total))
            print(len(productos))
            menu()
            raiz.mainloop()
    elif op == '2':
        raiz = Tk()
        rutainstrucciones = filedialog.askopenfilename(title="Abrir")
        Button(raiz, text= "abrir archivo").pack
        if rutainstrucciones != None:
            instrucciones()
            print("instrucciones cargadas")
            print(nombre)
            print(grafica)
            print(titulo)
            menu()
            raiz.mainloop()
    elif op == '3':
        graficar()
        menu()
    elif op == '4':
        reporte()
        print("reporte generado")
        menu()
    elif op == '5':
        exit()
    elif op == '6':
        print(barras,lineas,pie)

def instrucciones():
    global nombre, grafica, titulo, titulox, tituloy, x, y, total, pie, barras, lineas
    archivoInstrucciones = open(rutainstrucciones,'r')
    aI = archivoInstrucciones.read()
    nombre = re.findall('Nombre:.+".+"', aI, flags=re.IGNORECASE)
    grafica = re.findall('Grafica:.+".+"', aI, flags=re.IGNORECASE)
    titulo = re.findall('Titulo:.+".+"', aI, flags=re.IGNORECASE)
    titulox = re.search('Titulox:.+".+"', aI, flags=re.IGNORECASE)
    tituloy = re.search('Tituloy:.+".+"', aI, flags=re.IGNORECASE)
    barra = re.search('"Barras"', aI, flags=re.IGNORECASE)
    linea = re.search('"Lineas"', aI, flags=re.IGNORECASE)
    pies = re.search('"Pie"', aI, flags=re.IGNORECASE)
    if titulox != None:
        titulox = re.findall('Titulox:.+"', aI, flags=re.IGNORECASE)
        x = True
    else:
        x= False
    
    if tituloy != None:
        tituloy = re.findall('Tituloy:.+"', aI, flags=re.IGNORECASE)
        y = True
    else:
        y= False
    if barra != None:
        barras= True
        print("grafica de barras")
    if linea != None:
        lineas != True
        print("grafica de lineas")
    if pies != None:
        pie = True
        print("grafica de lineas")
    nombre = re.split('"',nombre[0])
    nombre= nombre[1]
    

def cargar_ventas():
    global Mes, año, productos, pie, barras, lineas, pmv, pMv, menor, mayor,unidades,precio
    archivoVentas = open(rutaventas,'r')
    aV = archivoVentas.read()
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

    productos= re.findall('".+"', aV)
    dat = re.split(',|\]',aV)
    precio = []
    unidades = []
    p = 1
    while len(dat)>p:
        d = float(dat[p])
        precio.append(d)
        p=p+3
    p = 2
    while len(dat)>p:
        d = float(dat[p])
        unidades.append(d)
        p=p+3
    p = 0
    while len(precio)>p:
        subtotal = precio[p]+unidades[p]
        p=p+1
        subtotal = "{0:.2f}".format(subtotal)
        subtotal = float(subtotal)
        total.append(subtotal)
        mayor()
    
def mayor():
    global unidades, productos, pmv, pMv
    mayor = 0
    for i in range(0, len(productos)):
        if unidades[i]>mayor:
            mayor = unidades[i]
            pmv = productos[i]
    menor = 1000000 
    for i in range(0, len(productos)):
        if menor>unidades[i]:
            menor = unidades[i]
            pMv = productos[i]

def graficar():
    global x,y,nombre,total,productos,titulo,titulox,tituloy
    nombreg = str(nombre)

    if barras == True:
        if x == True & y== True:
            fig, ax = plotpy.subplots()
            ax.bar(productos, total)
            ax.set_title(titulo)
            ax.set_xlabel(titulox)
            ax.set_ylabel(tituloy)
            plotpy.savefig(nombreg + '.jpg')
            plotpy.show()
            print("grafica de barras generada")
        else:
            fig,ax = plotpy.subplots()
            ax.bar(productos, total)
            ax.set_title(titulo)
            plotpy.savefig(nombreg + '.jpg')
            plotpy.show()
            print("grafica de barras generada")
    if lineas == True:
        if x == True & y== True:
            fig, ax = plotpy.subplots()
            ax.plot(productos, total)
            ax.set_title(titulo)
            plotpy.savefig(nombreg +'.jpg')
            plotpy.show()
            print("grafica de lineas generada")
        else:
            fig, ax = plotpy.subplots()
            ax.plot(productos, total)
            ax.set_title(titulo)
            ax.set_xlabel(titulox)
            ax.set_ylabel(tituloy)
            plotpy.savefig(nombreg + '.jpg')
            plotpy.show()
            print("grafica de lineas generada")
    if pie == True:
        if x == True & y== True:
            fig, ax = plotpy.subplots()
            ax.pie(total, labels=productos, autopct="%0.1f %%")
            ax.set_title(titulo)
            plotpy.savefig(nombreg + '.jpg')
            plotpy.show()
            print("grafica de pie generada")
        else:
            fig, ax = plotpy.subplots()
            ax.pie(total, labels=productos, autopct="%0.1f %%")
            ax.set_title(titulo)
            ax.set_xlabel(titulox)
            ax.set_ylabel(tituloy)
            plotpy.savefig(nombreg + '.jpg')
            plotpy.show()
            print("grafica de pie generada")
def reporte():
    global Mes, año
    nombreR = str(Mes)+str(año)+'.html'
    reporte = open(nombreR, 'w')
    dats = """<p style="text-align: center;"><span style="text-align: center; color: #0000ff;"><strong>Nombre: Cristian No&eacute; Axpuac Aspuac</strong></span><span style="text-align: center; color: #0000ff;"><strong>Carnet: 202004763</strong></span><span style="text-align: center; color: #0000ff;"><strong></strong></span><span style="text-align: center; color: #0000ff;"><strong></strong></span><span style="text-align: center; color: #0000ff;"><strong></strong></span></p>
    <p><span style="color: #00ff00;"><span style="text-align: left; color: #00ff00;"><span style="text-align: center; color: #0000ff;"><strong>Producto mas Vendido: """+str(pmv)+ """ Unidades.</strong></span></span></span></p>
    <p><span style="color: #00ff00;"><span style="text-align: left; color: #00ff00;"><span style="text-align: center; color: #0000ff;"><strong>Producto menos Vendido: """+str(pMv)+ """ Unidades.</strong></span></span></span></p>
    <table border="1" style="width: 100%; border-collapse: collapse; border-style: double;">
    <tbody>
    <tr>
    <td style="width: 13%; text-align: center;">No.</td>
    <td style="width: 27%; text-align: center;">Producto</td>
    <td style="width: 20%; text-align: center;">Precio</td>
    <td style="width: 20%; text-align: center;">Unidades</td>
    <td style="width: 20%; text-align: center;">Total</td>
    </tr>"""
    contador = 1
    for i in range(0,len(productos)):
        dats = dats+"""<tr>
        <td style="width: 13%; text-align: center;">"""+str(contador)+ """</td>
        <td style="width: 27%; text-align: center;">"""+str(productos[i])+"""</td>
        <td style="width: 20%; text-align: center;">"""+str(precio[i])+"""</td>
        <td style="width: 20%; text-align: center;">"""+str(int(unidades[i]))+"""</td>
        <td style="width: 20%; text-align: center;">"""+str(total[i])+"""</td>
        </tr>
        <tr>"""
        contador = contador+1
    reporte.write(dats)
    reporte.close()
    webbrowser.open_new_tab(nombreR)

menu()

