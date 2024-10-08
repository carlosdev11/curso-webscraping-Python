import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/"

#Doy informacion mia para protegerme de baneos
encabezado = {
    "user-agent":"google(windows 10)"
}

#Requerimiento al servidor
respuesta = requests.get(url, headers=encabezado)

#Parsea del arbol html con beautiful soup
soup = BeautifulSoup(respuesta.text)

contenedor_pregunta = soup.find(id="Questions") #"questions es como se llama el id que contiene todos los contenerdores"
print(contenedor_pregunta)
#lista_preguntas = contenerdor_pregunta.find_all('div', id="question-summary") #question-summary se llaman las cajas que contienen las preguntas (esta opcion no funciona porque esta mezclado con numeros cada uno de los id)
lista_preguntas = contenedor_pregunta.find_all('div', class_="s-post-summary") #Al tener los id diferentes, lo hago con las clases ya que si que son iguales (IMPORTANTE poner class_)

#Saco la informacion de los h3
for pregunta in lista_preguntas:
    descripcion_pregunta = pregunta.find('h3').text #Extraigo solo el texto de las etiquetas h3
    print(descripcion_pregunta)
    