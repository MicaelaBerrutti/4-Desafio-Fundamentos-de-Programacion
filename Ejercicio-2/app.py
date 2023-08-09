import requests
import json

capitales_latam = capitalesLatinoamerica = ['Buenos Aires', 'La Paz', 'Brasilia', 'Santiago', 'Bogotá', 'San José', 'La Habana', 'Santo Domingo', 'Quito', 'San Salvador', 'Ciudad de Guatemala', 'Tegucigalpa', 'Ciudad de México', 'Managua', 'Panamá', 'Asunción', 'Lima', 'San Juan', 'San Cristóbal', 'San Vicente', 'Kingstown', 'Paramaribo', 'Puerto España', 'Montevideo', 'Caracas']

archivo = "Ejercicio-2\documento.txt"


def mostrar_capital():

    with open(archivo, "w") as file: #Evitar duplicado 
        file.write("")

    capitales = []

    for capital in capitales_latam:

        if capital=="Santiago": #Evitar error concreto en la ubicación de esta capital
            datos_capital = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={capital},CL&appid=c28dc4a2dfc200d61575e65a801f8b48")
        else:
            datos_capital = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={capital}&appid=c28dc4a2dfc200d61575e65a801f8b48")

        resultados_capital = json.loads(datos_capital.text)
        latitud = resultados_capital[0]['lat']
        longitud = resultados_capital[0]['lon']

        
        datos_temperatura = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&lang=es&units=metric&appid=c28dc4a2dfc200d61575e65a801f8b48")

        resultados_temperatura = datos_temperatura.json()
        
        with open(archivo, "a") as file:
            file.write("Capital: " + capital + "\n" +
            "País: " + resultados_capital[0]['country'] + "\n" +
            "Característica del clima: " + resultados_temperatura['weather'][0]['description'] + "\n" +
            "Sensación térmica: " + str(resultados_temperatura['main']['feels_like']) + "°C \n" +
            "Presión: " + str(resultados_temperatura['main']['pressure']) + " hPA\n" +
            "Humedad: " + str(resultados_temperatura['main']['humidity']) + "% \n" +
            "Temperatura máxima: " + str(resultados_temperatura['main']['temp_max']) + " °C \n" +
            "Temperatura mínima: " + str(resultados_temperatura['main']['temp_min']) + "; \n\n")
        
    return(capitales)

mostrar_capital()
        
        

