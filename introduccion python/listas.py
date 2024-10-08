numeros = [9,3,6,8,1]

numeros.append(10) #añado el numero 10 al final de la lista
print(numeros)
numeros.remove(6) #elimino el numero que le diga de la lista
print(numeros)
numeros.sort() #devuelve el array ordenado de menor a mayor
print(numeros)
numeros.reverse() #devuelve el array ordenado de mayor a menor
print(numeros)
print(numeros[0]) #me muestra en pantalla en numero 9 (posicion 0)

#Recorro el array con un buvle for
for e in numeros:
    print(e)