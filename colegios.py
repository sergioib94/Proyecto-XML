def Listar (doc):
    lista = doc.xpath('//Centro/text()')
    return lista

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
    print ("0.Salir")
    print ("")

    opcion = input("opcion: ")

    if opcion == "1":
        print ("Listado de los colegios: ")
        for colegios in Listar (doc):
            print ("*",colegios)

    if opcion == "0":
        break;