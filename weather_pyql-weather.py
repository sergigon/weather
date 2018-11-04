# Info:
# https://www.pythoniza.me/pronostico-del-clima-con-python-y-yahoo/
# https://github.com/alexdzul/pyql-weather
# https://pyql-weather.readthedocs.io/es/latest/

from pyql.weather.forecast import Forecast

# Instanciamos un objeto del tipo Forecast utilizando la funcion get pasandole el parametro woeid y u
my_woeid = 24553135 # Where On Earth ID
forecast = Forecast.get(woeid=my_woeid, u="c") # "u" nos permite definir si la unidad de medida del clima deseada es en grados Celsius ("c") o Fahrenheit ("f")

####################################################################
# Location
print("Location:")
#print(forecast.location.city, forecast.location.region, forecast.location.country)
print("Ciudad: " + forecast.location.city)
print("Region: " + forecast.location.region)
print("Pais: " + forecast.location.country)
print("")

# Datos de la salida y puesta del sol
print("Datos de la salida y puesta del sol:")
print("Salida del sol: {0}".format(forecast.astronomy.sunrise))
print("Puesta del sol: {0}".format(forecast.astronomy.sunset))
print("")

# Atmosfera
print("Atmosfera:")
print("************** Atmosfera **********************")
print("Humedad: {0}".format(forecast.atmosphere.humidity))
print("Presion: {0}".format(forecast.atmosphere.pressure))
print("Incremento: {0}".format(forecast.atmosphere.rising))
print("Visibilidad: {0}".format(forecast.atmosphere.humidity))
print("***********************************************")
print("")

# Viento
print("Viento:")
print("Enfriamiento: {0}".format(forecast.wind.chill))
print("Direccion: {0}".format(forecast.wind.direction))
print("Velocidad: {0}".format(forecast.wind.speed))
print("")

# Unidades de medicion
print("Unidades de medicion:")
print("Unidad de velocidad: {0}".format(forecast.units.speed))
print("Unidad de presion: {0}".format(forecast.units.pressure))
print("Unidad de distancia: {0}".format(forecast.units.distance))
print("Unidad de temperatura: {0}".format(forecast.units.temperature))
print("")

# Condicion actual del clima
print("Condicion actual del clima:")
print("Codigo: " + forecast.item.condition.code)
print("Fecha: " + forecast.item.condition.date)
print("Temperatura: " + forecast.item.condition.temp)
print("Texto: " + forecast.item.condition.text)
print("")

print("####################################################################\n")
####################################################################

# Ejemplo unificado
print("Ejemplo unificado:")

# En el siguiente ejemplo uniremos varias partes de la libreria para presentar la informacion de una manera mas formal

ciudad = forecast.location.city
region = forecast.location.region
pais = forecast.location.country
print("Condiciones del clima en {0}, {1}, {2}:".format(ciudad, region, pais))
print("Fecha: {0}".format(forecast.item.condition.date))
print("Temperatura: {0} grados {1}".format(forecast.item.condition.temp, forecast.units.temperature))
print("Condicion: {0} ({1})".format(forecast.item.condition.text, forecast.item.condition.code))
print("")

print("####################################################################\n")
####################################################################

# Pronostico 5 dias

# Yahoo Weather nos permite conocer el pronostico del clima de 5 fechas continuas (incluyendo la fecha de consulta).

# Por ejemplo: Si consultamos el clima el dia de hoy 28-04-2015 (dia 1), Yahoo nos ofrecera el pronostico para los dias 29-04-2015 (dia 2), 30-04-2015 (dia 3), 01-05-2015 (dia 4) y 02-05-2015 (dia 5).

# A continuacion veremos un ejemplo basico para extraer el pronostico para la ciudad de Merida, Yuc, Mexico:

print("Pronostico 5 dias (raw):")
woeid = 133327
forecast = Forecast.get(woeid=woeid, u="c")
for day in forecast.item.forecast:
    print(day)
print("")

# Podemos observar que el resultado que pyql-weather retorna es un arreglo de objetos en formato json los cuales podemos manipular para formatear la informacion de la siguiente manera:

print("Pronostico 5 dias (ordenado):")
woeid = 133327
forecast = Forecast.get(woeid=woeid, u="c")
ciudad = forecast.location.city
region = forecast.location.region
pais = forecast.location.country
print("Condiciones del clima para la ciudad de {0}, {1}, {2}: \n".format(ciudad, region, pais))
for day in forecast.item.forecast:
    print("Fecha: {0} {1}".format(day['day'], day['date']))
    print("Pronostico: {0} ({1})".format(day['text'], day['code']))
    print("Temperatura Minima: {0} grados {1}".format(day['low'], forecast.units.temperature))
    print("Temperatura Maxima: {0} grados {1}".format(day['high'], forecast.units.temperature))
    print("*****************************************************************************")
