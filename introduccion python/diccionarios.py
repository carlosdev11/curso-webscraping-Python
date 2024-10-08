diccionario = {}

#añado valores al diccionario
diccionario["nombre"] = "Carlos"
diccionario["edad"] = 22
print(diccionario)

#Obtengo la edad solo (2 opciones)
print(diccionario["edad"])
print(diccionario.get("edad"))

diccionario2 = {5.1: 10 , "vocales":["a","e","i","o","u"]}
print(diccionario2)
print(len(diccionario2)) #muestra los elementos en el diccionario (2 elementos)
del(diccionario2[(5.1)]) #elimino el valor 5.1
print(diccionario2) 
