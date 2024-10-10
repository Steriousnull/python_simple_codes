import requests

city_name = "New Delhi"

#your api key which you can get from https://home.openweathermap.org/api_keys
API_key = ""
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    print('Yes, You Got the data')
    data = response.json()
    print(data)  # Print the data
    print('weather is : ', data['weather'][0]['description'])
    print('current temperature is : ', data['main']['temp'])
    print('current feels like is : ', data['main']['feels_like'])
    print('humidity is : ', data['main']['humidity'])


else:
    print(f"Failed to get data. Status code: {response.status_code}")
    print(f"Response: {response.text}")  # Print the response text
