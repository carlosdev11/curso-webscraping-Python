import requests
from lxml import html

url = "https://es.wikipedia.org/"
encabezado = {
    "user-agent":"google(windows 10)"
}

respuesta = requests.get(url , headers = encabezado)

parser = html.fromstring(respuesta.text) #nos parsea lo que hay en la variable respuesta

portada = parser.get_element_by_id("firstHeading")  #Obtengo el elemento por id
#portada = parser.xpath("//a[@id='firstHeading']/text()") # Otra opción, devuelve lo mismo que el anterior

print(portada.text_content()) #miuestra como resultado Wikipedia:Portada