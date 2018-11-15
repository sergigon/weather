import requests
api_key = '9838870ce6324daf95d161656180811'

# Constant names
apixu_limit_weather = 2 # 7 days limit
apixu_month_limit_calls = 10000 # 10000 limit calls per month

# Variable names
location = "Guadalajara, Spain"
order = "weather"

url_current = 'http://api.apixu.com/v1/current.json'
url_forecast = 'http://api.apixu.com/v1/forecast.json'
url_test = 'https://api.github.com/events'

params = {
	'key': api_key,
	'q': location,
	'days': apixu_limit_weather, # Only for forecast
	'lang': 'es'
}

r = requests.get(url_forecast, params = params)

#print(r.url)

data = r.json()

print (data['location']['country'])