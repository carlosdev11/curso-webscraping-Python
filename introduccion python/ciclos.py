# CICLOS FOR 
import random
"""
x = 0
for i in range(10): # las veces que quiero que se haga el bucle
    print(i)
    x += random.randint(1,5) # sumo 5 numeros de los que hace el bucle (entre 0 y 9)
print(x)
"""



# CICLOS WHILE
x = 0
contador = 0
while x != 5: #Cuando x valga 5 la condicion dara False y se saldra del bucle
    x = random.randint(1,100)
    contador += 1
    print(str(x) + " -> " + str(contador))
print(x)