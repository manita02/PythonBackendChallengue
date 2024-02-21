import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()
            temperature = data['main']['temp']
            print("The current temperature in the city of '"+ data['name'] +"' is: "+ str(temperature) +" °C")
            return temperature > 28
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the HTTP request:", e)
            return False
        except KeyError as e:
            print("An error occurred while processing the API response:", e)
            return False

print(GeoAPI.is_hot_in_pehuajo())