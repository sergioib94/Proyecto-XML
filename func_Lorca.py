import math

def Listar (doc):
    lista = doc.xpath('//Centro/text()')
    return lista

def Contar (doc):
    return int(doc.xpath('count(//Centro)')) - int(doc.xpath('count(//Contacto/Web)'))

def Filtrar (cadena,doc):
    datos = []
    colegios = {}
    contactos = []

    for centro in doc.xpath('//Centro[contains(text(),"%s")]/text()' %cadena):
        colegios["Nombre"] = centro

    for contacto in doc.xpath('//colegio_lorca[Centro = Centro[contains(text(),"%s")]/text()]/./Contacto/*/text()' %cadena):
        contactos.append(contacto)
        colegios["Contactos"] = contactos

    for contacto2 in doc.xpath('//instituto_lorca[Centro = Centro[contains(text(),"%s")]/text()]/./Contacto/*/text()' %cadena):
        contactos.append(contacto2)
        colegios["Contactos"] = contactos
    
    #return (colegios,contactos)

    datos.append(colegios)

    return datos

    # hacer una lista de diccionarios y en cada diccionario una lista con los contactos. ej: [{A},{B},...] y dentro de los diccionarios {"colegio":"A", "Contactos":[lista de contactos]}

def Buscar (pedania,doc):
    pedanias = doc.xpath ('//Localizacion[Pedania="%s"]/../Centro/text()' %pedania)
    return pedanias

def Distancias (parque,doc,doc2):
    origen = []
    destinos = []

    for la in doc2.xpath('//parques[situacion="%s"]/./latitud/text()' %parque):
        origen.append(la)
    for lo in doc2.xpath('//parques[situacion="%s"]/./longitud/text()' %parque):
        origen.append(lo)

    destino = doc.xpath('//Coordenadas/*/text()')

    #(lat1, lon1, lat2, lon2)
    #rad=math.pi/180
    #dlat=lat2-lat1
    #dlon=lon2-lon1
    #R=6372.795477598 #radio de la tierra
    #a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    #distancia=2*R*math.asin(math.sqrt(a))
    #return distancia

    return destino

    #Ayuda (listado de pedanias de lorca)

def Listado_pedanias(doc):
    pedanias = doc.xpath('//Localizacion/Pedania/text()')
    repeticiones = list(set(pedanias))
    return repeticiones
