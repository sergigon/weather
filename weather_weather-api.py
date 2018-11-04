# Info: https://pypi.org/project/weather-api/
from weather import Weather, Unit

# Weather con woeid:
"""
print("Weather con woeid:")
weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup(560743)
condition = lookup.condition
print(condition.text)
print("")
"""

# Weather con location name
"""
print("Weather con location name:")
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('dublin')
condition = location.condition
print(condition.text)
print("")
"""

# Weather upcoming days

print("Weather upcoming days:")
weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('dublin')
forecasts = location.forecast
for forecast in forecasts:
	print(forecast.text)
	print(forecast.date)
	print(forecast.high)
	print(forecast.low)
print("")

# Info clases y metodos
## Objeto de tipo Weather
weather = Weather(unit=Unit.CELSIUS)
'''
########################################################################
# Metodos
# - lookup(woied): Retorna objeto de tipo WeatherObject
# - lookup_by_location(location): Retorna objeto de tipo WeatherObject
# - lookup_by_latlng(latlng): Retorna objeto de tipo WeatherObject
########################################################################
'''
## Objeto de tipo WeatherObject
weatherobject = weather.lookup_by_location('madrid')
'''
########################################################################
# Metodos:
# - last_build_date(): Retorna string; Fecha y hora actual
# - title(): Retorna string; "Yahoo! Weather - Leganes, Madrid, ES"
# - description(): Retorna string; "Yahoo! Weather for Leganes, Madrid, ES"
# - language(): Retorna string; Lenguaje
# - astronomy(): Retorna objeto de tipo Astronomy
# - atmosphere(): Retorna objeto de tipo Atmosphere
# - image(): Retorna string; Datos en JSON sobre la imagen
# - condition(): Retorna objeto de tipo Condition
# - units(): Retorna objeto de tipo Unit
# - forecast(): Retorna vector de onjetos de tipo Forecast
# - latitude(): Retorna string; Latitud
# - longitude(): Retorna string; Longitud
# - location(): Retorna objeto de tipo Location
# - wind(): Retorna objeto de tipo Wind
# - print_obj(): Retorna string; Datos en JSON de todo el objeto
########################################################################
'''
show = False
if (show): # Muestro info de los metodos de WeatherObject
	print("\n -- weatherobject.last_build_date:")
	print(weatherobject.last_build_date)
	print("\n -- weatherobject.title:")
	print(weatherobject.title)
	print("\n -- weatherobject.description:")
	print(weatherobject.description)
	print("\n -- weatherobject.language:")
	print(weatherobject.language)
	print("\n -- weatherobject.astronomy:")
	print(weatherobject.astronomy)
	print("\n -- weatherobject.atmosphere:")
	print(weatherobject.atmosphere)
	print("\n -- weatherobject.image:")
	print(weatherobject.image)
	print("\n -- weatherobject.condition:")
	print(weatherobject.condition)
	print("\n -- weatherobject.unit:")
	print(weatherobject.units)
	print("\n -- weatherobject.forecast:")
	print(weatherobject.forecast)
	print("\n -- weatherobject.latitude:")
	print(weatherobject.latitude)
	print("\n -- weatherobject.longitude:")
	print(weatherobject.longitude)
	print("\n -- weatherobject.location:")
	print(weatherobject.location)
	print("\n -- weatherobject.wind:")
	print(weatherobject.wind)
	print("\n -- weatherobject.print_obj:")
	print(weatherobject.print_obj)


# Weather by typing location (in progress)
"""
condition = weatherobject.condition # Objeto de tipo Condition (date, text, code, temp)
print(condition.text)

location_name = raw_input("Enter a name: ")
print(location_name)
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location(str(location_name))
print(location.text)
print(location.date)
print(location.high)
print(location.low)

try:
	location = weather.lookup_by_location(str(location_name))
	forecasts = location.forecast
	print(forecast.text)
except NameError:
	print("Localizacion no valida")

except:
	print("Localizacion vacia")

else:
	print("Cogio bien el lugar")
	print("El lugar es: " + location_name)
"""
