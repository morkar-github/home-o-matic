class OpenWeather:
    def __init__(self, apiKey):
        self._apiKey = apiKey
        
        def getTemperature():
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2923544&units=metric&APPID=' + self._apiKey) #abcc6a6d692594e4c9524d7088d5184b
        responseAsJson = response.json()
        jsonNode = responseAsJson['main']
        temperature     = float(jsonNode['temp'])
        temperature_min = float(jsonNode['temp_min'])
        temperature_max = float(jsonNode['temp_max'])
        
        return temperature, temperature_min, temperature_max
