from lxml import etree
from func_Lorca import *
doc = etree.parse ('colegios_lorca.xml')

from lxml import etree
doc2 = etree.parse ('parques_lorca.xml')

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
            print (datos["Nombre"])
            print (datos["Contactos"])
    
    if opcion == "4":
        pedania = input("Introduce una pedania: ")

        print ("Colegios de la pedania: ")
        print ("")

        for pedanias in Buscar (pedania,doc):
            print ("*",pedanias)
    
    if opcion == "5":
        parque = input("Introduce nombre del parque: ")
        #km = int(input("Radio de cercania: "))

        print(Distancias(parque,doc,doc2))

    if opcion == "6":
        print ("Estas son las pedanias de Lorca:")
        for i in Listado_pedanias(doc):
            print ("*",i)

    if opcion == "0":
        break;