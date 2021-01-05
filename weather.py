#pip install pyfiglet
#pip install requests
import pyfiglet
import requests
ascii_banner = pyfiglet.figlet_format("weather")
print(ascii_banner)

api_address = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input("Hi, What is your city name?: \n")
url = api_address + city
 
json_data = requests.get(url).json()
formatted_data  = json_data['weather'][0]['main']
print(formatted_data)
