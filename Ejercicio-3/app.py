import requests
import pandas as pd
import json

archivo_paises =(pd.read_csv("Ejercicio-3/all.csv")) 
archivo_capitales =(pd.read_csv("Ejercicio-3/country-list.csv"))
pais_seleccionado = input("Ingrese un país o paises separados por coma ")

pais_array = str(pais_seleccionado).split(", ")

def obtener_ISO(pais): #obtener código ISO del país para poder utilizar la API para obtener coordenadas
    seleccion = archivo_paises.loc[archivo_paises['name'] == str(pais).capitalize()] 
    return(seleccion['alpha-2'].iloc[0])

def obtener_capital(pais): #obtener capital de país para poder utilizar API
    seleccion = archivo_capitales.loc[archivo_capitales['country'] == str(pais).capitalize()]
    return(seleccion['capital'].iloc[0])


def obtener_dict(pais_array): #se genera un diccionario donde la key es el código ISO del país y la capital es la value.
    
    pais_iso = {}
    
    for pais in pais_array:
        iso = str(obtener_ISO(pais))
        capital = obtener_capital(pais)
        pais_iso[iso] = capital
    return pais_iso

         
def obtener_datos_pais(pais):
    dict_pais = obtener_dict(pais)
    lista_paises = []
    for pais in pais_array:
        iso = str(obtener_ISO(pais))
        capital = str(dict_pais[iso]) #se utiliza la key código ISO para acceder a la value(capital) que corresponde

        datos_coordenadas = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={capital},{iso}&appid=c28dc4a2dfc200d61575e65a801f8b48")
        respuesta_coordenadas = json.loads(datos_coordenadas.text)
        latitud = respuesta_coordenadas[0]['lat']
        longitud = respuesta_coordenadas[0]['lon']

        datos_temperatura = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&lang=es&units=metric&appid=c28dc4a2dfc200d61575e65a801f8b48")

        resultados_temperatura = datos_temperatura.json()

        datos = ("País : "+ str(resultados_temperatura['sys']['country']) + ' \n'+ "Temperatura actual: " + str(resultados_temperatura['main']['temp']) + '°C\n'+
                    "Temperatura máxima: " + str(resultados_temperatura['main']['temp_max']) + " °C\n "+
                    "Temperatura mínima: " + str(resultados_temperatura['main']['temp_min']) + "°C\n "+
                    "Descripción del clima: " + str(resultados_temperatura['weather'][0]['description']) + "\n ")
        lista_paises.append(datos)
    return lista_paises

def obtener_salida(pais_array):
    temperatura_pais = obtener_datos_pais(pais_array)
    for item in temperatura_pais:
        print(item)
    
    with open("Ejercicio-3\salida.txt", "w") as archivo: #Se imprime el output en un documento txt para mayor comodidad al visualizar los datos 
        for item in temperatura_pais:
            archivo.write(item)

   
try:
    obtener_salida(pais_array)
except:
    print("Entrada no válida")