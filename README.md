# Desafío 4: Fundamentos de Programación

<b>Breve explicación de cada ejercicio:</b>

En el primer ejercicio, utilicé los dos lenguajes (js y py) proporcionando la solución para cada uno de ellos. El programa se basa en una función(buscar_valor) que recibe dos parámetros: el array el cuál se va a iterar y el número el cuál se buscará en el array. En cada iteración del for se comparará el elemento del array con el número objetivo, retornando el índice de la primera aparición. En caso de que terminada la iteración de todos los valores del array no se encuentre el número objetivo, se retorna -1 indicado en el return fuera del for.

El ejercicio 2 se basa en la utilización de la API <a href="https://openweathermap.org/current"> Current weather data</a> y la API <a href="https://openweathermap.org/api/geocoding-api"> Geocoding API </a> para obtener información climática de las capitales de los países latinoamericanos.
Para hacer esto, partí de un array con las capitales latinoamericanas y realicé un recorrido a este array con la función mostrar_capital() para obtener los datos necesarios y escribirlos en un documento(documento.txt). Utilicé la API Geocoding de OpenWeatherMap para obtener las coordenadas de cada capital, para luego poder utilizar la API Current weather data y obtener las respuestas de los datos climáticos.
La primer API devuelve un archivo json con los datos de la ciudad, de estos datos seleccioné la latitud y longitud de la misma, que es lo que se necesita para utilizar la api Current weather data:
latitud = resultados_capital[0]['lat']
longitud = resultados_capital[0]['lon']

Con estos datos utilicé la API de Current weather data para obtener los datos de temperatura, realizando la selección de datos del archivo json que devuelve la consulta a la api. Utilice open en modo a (append) para agregar la información requerida de cada capital en el documento especificado.

El ejercicio 3 tiene el objetivo de retornar datos del clima de un país o lista de países que recibe como input. La función obtener_salida recibe un país(o varios paises separados por comas) como parámetro y retorna: código ISO del país, temperatura actual, máxima y mínima, y descripción del clima del país/ países.
Para realizar esto comencé utilizando dos archivos csv para poder obtener una ciudad de país seleccionado(en este caso la capital) para poder utilizar la api Geocoding y obtener como respuesta las coordenadas de la ciudad. Utilicé pandas para obtener la capital y por otro lado el código ISO del país(necesario para realizar la consulta a la API Current weather data).
Con el código ISO y con la capital del país se genera un diccionario, donde la  key es el código ISO del país y la capital es la value. Esto se utiliza en la función obtener_datos_pais, donde se utiliza el iso del país para acceder a la capital correspondiente y poder realizar las consultas a las APIs. Primero a API Geocoding, donde realicé la selección de los datos que corresponden a longitud y latitud. Luego conociendo estos datos se realiza la consulta a la API Current weather data y se selecciona los datos a mostrar de la respuesta json. 
