from influxdb import InfluxDBClient

class WeatherDAO:
    def __init__(self):
        self._database = InfluxDBClient(database=databaseName)
        
        def saveTemperature(self, temperature, minimum, maximum):
        json =
        [
        	{
         "measurement": "openweather",
         "fields":
         {
         "temperature": temperature,
         "temperature_min": minimum,
         "temperature_max": maximum
         }
        	}
         ]
        self._database.write_points(json)
