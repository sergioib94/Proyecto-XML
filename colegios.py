import math

def Listar (doc):
    lista = doc.xpath('//Centro/text()')
    return lista

def Contar (doc):
    return int(doc.xpath('count(//Centro)')) - int(doc.xpath('count(//Contacto/Web)'))

def Filtrar (cadena,doc):
    colegios = []
    contactos = []

    for colegio in doc.xpath('//Centro[contains(text(),"%s")]/text()' %cadena):
        colegios.append(colegio)

    for contacto in doc.xpath('//colegio_lorca[Centro = Centro[contains(text(),"%s")]/text()]/./Contacto/*/text()' %cadena):
        contactos.append(contacto)

    for contacto2 in doc.xpath('//instituto_lorca[Centro = Centro[contains(text(),"%s")]/text()]/./Contacto/*/text()' %cadena):
        contactos.append(contacto2)
    
    return (colegios,contactos)

def Buscar (pedania,doc):
    pedanias = doc.xpath ('//Localizacion[Pedania="%s"]/../Centro/text()' %pedania)
    return pedanias

def Distancias (doc,doc2,km):
    #(lat1, lon1, lat2, lon2)
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

from lxml import etree
doc = etree.parse ('colegios_lorca.xml')

while True:
    print ("")
    print ("Menu Principal:")
    print ("")
    print ("1.Listar informacion: Mostrar los colegios que hay en Lorca.")
    print ("2.Contar informacion: Contar los colegios que hay en Lorca que no cuenten con pagina web.")
    print ("3.Buscar o Filtrar informacion: Meter por teclado un nombre o parte de el y mostrar los contactos de esos colegios.")
    print ("4.Buscar informacion relacionada: Introducir por teclado una pedania y decir que colegio hay en esa pedania.")
    print ("5.Ejercicio Libre: Meter el nombre de un colegio o bien el nombre de un parque y usando las coordenadas y las coordenadas de un segundo fichero(parques de lorca), mostrar que parques estan cerca de algun colegio o que colegios tienen parques cerca.")
    print ("6.Ayuda XML (listado de pedanias)")
    print ("0.Salir")
    print ("")

    opcion = input("opcion: ")

    if opcion == "1":
        print ("Listado de los colegios: ")
        print ("")
        for colegios in Listar (doc):
            print ("*",colegios)

    if opcion == "2":
        print (Contar(doc),"colegios no cuentan con pagina web")

    if opcion == "3":
        cadena = input("Introduce una cadena: ")

        for datos in Filtrar(cadena,doc):
            for i in datos:
                print (i)
    
    if opcion == "4":
        pedania = input("Introduce una pedania: ")

        print ("Colegios de la pedania: ")
        print ("")

        for pedanias in Buscar (pedania,doc):
            print ("*",pedanias)
    
    if opcion == "5":
        pedania = input("Introduce la pedania: ")
        km = int(input("Radio de cercania: "))

        

    if opcion == "0":
        break;