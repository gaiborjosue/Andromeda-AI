import pyowm

owm = pyowm.OWM('0f099a9d2d31309d0cd5667ff52f18dc')

location = owm.weather_at_place("Ambato")
weather = location.get_weather()

temp = weather.get_temperature('celsius')
humidity = weather.get_humidity()

print(temp)
print(humidity)