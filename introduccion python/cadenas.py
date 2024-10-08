cadena = "el perro corre rapido"
cadena2 = "el perro corre lento"
cadena3 = "HOLAAAAAAAA"

#muestro la frase dos veces
print(cadena*2)

#muestro la primera letra de la frase
print(cadena[0])

#muestro la ultima letra de la frase
print(cadena[-1])

#muestro las letras de la 0 a la 5 (el pe)(los espacios blancos cuentan)
print(cadena[0:5])

#Metodos de cadenas
print(len(cadena)) #Muestra la longitud de la frase (los espacios tambien)
print(cadena.find("o")) #Le paso la letra que quiero buscar y me devuelve en que posicion está la primera "o"
print(cadena.rfind("o")) #Me dice la posicion del ultimo caracter que le digo
print(cadena3.lower()) #convierto la cadena en minusculas
print(cadena.upper()) #a mayusculas
print(cadena3.islower()) #verifica si TODA la cadena esta en minusculas
print(cadena.capitalize()) #Pongo la primera letra en mayuscula
print(cadena.replace("e","a")) #reemplazo todos los caracteres (las "e" por "a")
print(cadena.replace("e","a",2)) #reemplazo las primeras 2 "e" por "a"